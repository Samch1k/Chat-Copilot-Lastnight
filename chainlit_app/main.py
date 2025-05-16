import chainlit as cl
from llm import nl_to_sql, ask_llm
from db import execute_sql
import os

# Set default environment variables
os.environ.setdefault('PORT', '8080')

@cl.on_message
async def main(message: cl.Message):
    # Преобразуем NL в SQL
    sql_query = await nl_to_sql(message.content)
    # Выполняем SQL
    result = execute_sql(sql_query)
    # Отправляем результат пользователю
    await cl.Message(content=str(result)).send()
