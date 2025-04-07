from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

key = "Cz9NYayr9SOJoJGvesm69SliC8eO5kISEmOxEDfupk6MgG7KvwUpJQQJ99BDACZoyfiXJ3w3AAAAACOGXewy"
endpoint = "https://analise-sentimentos.openai.azure.com/"

def authenticate_client():
    credential = AzureKeyCredential(key)
    client = TextAnalyticsClient(endpoint=endpoint, credential=credential)
    return client

def analisar_sentimentos(client, documentos):
    resposta = client.analyze_sentiment(documents=documentos)
    resultados = [doc for doc in resposta if not doc.is_error]
    
    for i, resultado in enumerate(resultados):
        print(f"Frase: {documentos[i]}")
        print(f"Sentimento: {resultado.sentiment}")
        print(f"Confiança: Positivo={resultado.confidence_scores.positive:.2f}, "
              f"Neutro={resultado.confidence_scores.neutral:.2f}, "
              f"Negativo={resultado.confidence_scores.negative:.2f}")
        print("-" * 50)

def main():
    client = authenticate_client()

    with open("inputs/frases.txt", "r", encoding="utf-8") as arquivo:
        documentos = [linha.strip() for linha in arquivo if linha.strip()]

    analisar_sentimentos(client, documentos)

if __name__ == "__main__":
    main()
