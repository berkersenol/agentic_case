from agentic_patterns.reflection_pattern.reflection_agent import ReflectionAgent

agent = ReflectionAgent()

final_response = agent.run(
    user_msg="Write a short story about a lighthouse keeper",
    generation_system_prompt="You are a Python programmer tasked with generating high quality Python code",
    reflection_system_prompt="You are Andrej Karpathy, an experienced computer scientist",
    n_steps=10,
    verbose=1,
)

print("\n\n=== FINAL ===\n")
print(final_response)