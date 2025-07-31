from logging import config
import os
from dotenv import load_dotenv
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel,trace
from agents.run import RunConfig
import asyncio
import requests
from connection import config


load_dotenv()


lyrical_agent = Agent(name="lyrics agent", instructions="You analyze lyrical poetry. Focus on personal emotions, first-person perspective, song-like qualities, and mood.")

narative_agent = Agent(name="narative agent", instructions="You analyze narrative poetry. Identify the story, plot, characters, and thematic elements.")

daramatic_agent = Agent(name="daramatic agent", instructions="You analyze dramatic poetry. Examine dialogue, character interactions, and performative aspects.")

#user_input = input("Enter an instruction")
triage_agent = Agent(name ="triage-agent", instructions = """"
    You are a poetry triage expert. Determine the type of poem provided
    
    """,
     handoffs=[lyrical_agent, narative_agent, daramatic_agent])
                     
 
async def main():
    
    with trace("poetry"):
    
    
    
      result = await Runner.run(triage_agent,"""Warren,’ she said, ‘he has come home to die:
    You needn’t be afraid he’ll leave you this time.’
    ‘Home,’ he mocked gently.
    ‘Yes, what else but home?
    It all depends on what you mean by home.
    Of course he’s nothing to us, any more
    Than was the hound that came a stranger to us
    Out of the woods, worn out upon the trail.’
    ‘Home is the place where, when you have to go there,
    They have to take you in""", 
    run_config = config
    )
    
 
    
    print(result.final_output)
    
    print(result.last_agent)
    
# Run the async main function
if __name__ == "__main__":
    asyncio.run(main())