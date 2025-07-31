import os
from dotenv import load_dotenv
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, function_tool
from connection import config
from agents.run import RunConfig
import asyncio
import requests

# Load environment variables
load_dotenv()

# Define specialized agents
lyrical_agent = Agent(
    name="lyrics agent",
    instructions="You analyze lyrical poetry. Focus on personal emotions, first-person perspective, song-like qualities, and mood."
)

narrative_agent = Agent(
    name="narative agent",
    instructions="You analyze narrative poetry. Identify the story, plot, characters, and thematic elements."
)

dramatic_agent = Agent(
    name="daramatic agent",
    instructions="You analyze dramatic poetry. Examine dialogue, character interactions, and performative aspects."
)

# Define triage agent with explicit routing instructions
triage_agent = Agent(
    name="triage-agent",
    instructions="""
    You are a poetry triage expert. Determine the type of poem provided:
    - Lyrical: Expresses personal emotions (first-person, song-like, focused on mood).
    - Narrative: Tells a story (clear plot, characters, sequence of events).
    - Dramatic: Features dialogue/characters (meant to be spoken/performed).

    Output EXACTLY one of these agent names:
    - "lyrics agent" for lyrical poems
    - "narative agent" for narrative poems
    - "daramatic agent" for dramatic poems

    Example: For a poem with dialogue between characters, output "daramatic agent".
    """,
    handoffs=[lyrical_agent, narrative_agent, dramatic_agent]
)

async def main():
    poem = """Warren,’ she said, ‘he has come home to die:
    You needn’t be afraid he’ll leave you this time.’
    ‘Home,’ he mocked gently.
    ‘Yes, what else but home?
    It all depends on what you mean by home.
    Of course he’s nothing to us, any more
    Than was the hound that came a stranger to us
    Out of the woods, worn out upon the trail.’
    ‘Home is the place where, when you have to go there,
    They have to take you in.’"""

    # Run the triage agent
    result = await Runner.run(
        triage_agent,
        poem,
        run_config=config
    )
    print(result.final_output)

# Run the async main function
if __name__ == "__main__":
    asyncio.run(main())