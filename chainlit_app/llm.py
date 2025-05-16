import os
import openai

openai.api_key = os.environ["OPENAI_API_KEY"]

async def nl_to_sql(nl_query):
    # Пример запроса к GPT-4o для генерации SQL
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "Преобразуй запрос пользователя в безопасный SQL для анализа проектной базы данных."},
            {"role": "user", "content": nl_query}
        ],
        temperature=0.2
    )
    sql = response["choices"][0]["message"]["content"]
    return sql

async def ask_llm(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )
    return response["choices"][0]["message"]["content"]
