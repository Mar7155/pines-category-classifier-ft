'''
    ¿Dónde ocurre el embedding?


        El modelo contiene internamente una capa de embeddings (nn.Embedding) que mapea cada ID de token a un vector denso.

        En BERT y derivados (bert-base, distilbert-base…), la clase BertEmbeddings o DistilBertEmbeddings hace esto.

        Esta capa convierte cada entero (p. ej. el token 2003) en un vector de dimensión 768 (en DistilBERT).

        Luego esos embeddings se enriquecen con embeddings de posición y segment IDs.

        Durante el entrenamiento (fine-tuning)

        La capa de embeddings sí se actualiza junto con las demás capas del transformer, a menos que la congeles explícitamente.

        Eso significa que tus mensajes de spam/ham generan gradientes que ajustan las representaciones vectoriales.

    Resumen

        El embedding ocurre dentro del modelo preentrenado, no en tu función tokenize.

        La línea clave es cuando se inicializa el AutoModelForSequenceClassification, porque ese objeto incluye la capa de embeddings.

        En Hugging Face, no necesitas crear embeddings manuales: la llamada al modelo ya los genera.

   


Batch size = número de ejemplos que se procesan antes de actualizar los pesos del modelo.

        * per_device_train_batch_size especifica cuántos ejemplos procesa cada dispositivo en paralelo.

        * Si tienes varias GPU, el batch size total efectivo será:

        * batch_size_total=per_device_train_batch_size × numero_de_dispositivos

        * Si tienes 2 GPUs, el batch size total será:
                8 × 2 = 16 muestras por iteración.

    Consejos prácticos

        * Si tu GPU se queda sin memoria (CUDA out of memory), reduce el valor, por ejemplo a 4 o 2.

        * Si tienes memoria de sobra, puedes aumentarlo para acelerar el entrenamiento.

        * También puedes usar gradient_accumulation_steps para simular un batch más grande sin usar más memoria:




DistilBERT is pretrained by knowledge distillation to create a smaller model with faster inference and requires less compute to train. 
Through a triple loss objective during pretraining, language modeling loss, distillation loss, cosine-distance loss, DistilBERT 
demonstrates similar performance to a larger transformer language model.

'''


import pandas as pd
from datasets import Dataset
from sklearn.model_selection import train_test_split
from transformers import (
    AutoTokenizer,
    AutoModelForSequenceClassification,
    TrainingArguments,
    Trainer,
    DataCollatorWithPadding
)
# A Symphony of Rage
# 1. Cargar CSV
df = pd.read_csv("datasets\ms_pines_funcion_2000ejemplos.csv", encoding="utf-8")[["v1", "v2"]]
df = df.rename(columns={"v1": "label", "v2": "text"})
df["label"] = df["label"].map({"decorativo": 0, "coleccionable": 1, "promocional": 2, "funcional": 3})  # Mapear etiquetas a 0 y 1

# 2. Dividir en train/test
train_df, test_df = train_test_split(df, test_size=0.2, random_state=42)

# 3. Convertir a Dataset
train_dataset = Dataset.from_pandas(train_df)
test_dataset = Dataset.from_pandas(test_df)

# 4. Tokenizador
model_name = "distilbert-base-uncased" #La principal ventaja de este modelo de IA es su rendimiento. Requiere menos recursos computacionales
tokenizer = AutoTokenizer.from_pretrained(model_name)

def tokenize(batch):
    return tokenizer(batch["text"], padding="max_length", truncation=True)

train_dataset = train_dataset.map(tokenize, batched=True)
test_dataset = test_dataset.map(tokenize, batched=True)

train_dataset = train_dataset.rename_column("label", "labels")
test_dataset = test_dataset.rename_column("label", "labels")

train_dataset.set_format("torch", columns=["input_ids", "attention_mask", "labels"])
test_dataset.set_format("torch", columns=["input_ids", "attention_mask", "labels"])

# 5. Definir mapeo de etiquetas
id2label = {0: "decorativo", 1: "coleccionable", 2: "promocional", 3: "funcional"}
label2id = {"funcional": 0, "promocional": 1, "coleccionable": 2, "decorativo": 3}

# 6. Cargar modelo con etiquetas personalizadas
model = AutoModelForSequenceClassification.from_pretrained(
    model_name,
    num_labels=4,
    id2label=id2label,
    label2id=label2id,
)

# 7. Configuración de entrenamiento (usa evaluation_strategy)
training_args = TrainingArguments(
    output_dir="./results",
    #evaluation_strategy="epoch",
    save_strategy="epoch",
    learning_rate=2e-5,
    per_device_train_batch_size=2,  #Este parámetro puede generar problemas de memoria insuficiente
    per_device_eval_batch_size=2,
    num_train_epochs=5,
    weight_decay=0.01,
    logging_dir="./logs",
    logging_steps=50,
)

data_collator = DataCollatorWithPadding(tokenizer=tokenizer)

# 8. Entrenador
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=test_dataset,
    data_collator=data_collator  
)

# 9. Entrenar
trainer.train()

# 10. Evaluar
metrics = trainer.evaluate()
print("Resultados de evaluación:", metrics)

# 11. Guardar modelo y tokenizer
trainer.save_model("./ms_pines_funcion_classifier")
tokenizer.save_pretrained("./ms_pines_funcion_classifier")
