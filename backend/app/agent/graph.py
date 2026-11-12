"""Graph wiring: turns nodes + edges into a compiled, checkpointed agent.

SHOULD CONTAIN
- `build_graph(checkpointer)`:
    - StateGraph(AgentState)
    - add nodes: "agent", "confirm", "tools"
    - edges: START -> agent; conditional agent -> {confirm, tools, END} via route_after_agent;
      conditional confirm -> {tools, agent} via route_after_confirm; tools -> agent
    - compile(checkpointer=checkpointer) and return it
- It should read exactly like the agent-graph diagram in the spec. If it doesn't, one of them is wrong.

TIP
- Print `graph.get_graph().draw_mermaid()` once and compare it with your spec diagram.

AVOID
- Using the prebuilt `create_react_agent` here. Wire it by hand to learn nodes and edges. (Compare afterwards.)
"""
