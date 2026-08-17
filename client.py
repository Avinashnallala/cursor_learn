from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.agents import create_agent
from langchain_groq import ChatGroq

from dotenv import load_dotenv

load_dotenv()

import asyncio

async def main():
    client=MultiServerMCPClient(
        {
            'math':{
                'command':'python',
                'args':['mathserver.py'],
                'transport':'stdio'

            },
            'weather':{
                'url':'http://localhost:8000/mcp',
                'transport':'streamable_http'

            }
        }
    )

    import os

    os.environ['Groq_API_Key']=os.getenv('Groq_API_Key')

    tools=await client.get_tools()

    model=ChatGroq(model="openai/gpt-oss-120b")

    agent=create_agent(
    model=model,
    tools=tools
    )

    math_response= await agent.ainvoke(
        {
            'messages':[{'role':'user','content':'what is (3+5)*12?'}]
        }
    )

    print('math response:',math_response['messages'][-1].content)

    weather_response= await agent.ainvoke(
        {
            'messages':[{'role':'user','content':'what is the weather in california?'}]
        }

    )

    print('weather_response:',weather_response['messages'][-1].content)

asyncio.run(main())

