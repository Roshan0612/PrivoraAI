# PrivoraAI
PrivoraAI lets AI agents securely access a user's private data across applications through identity, authorization, OAuth, MCP, and provider connectors.


                  AUTHRYAI
       Identity-Aware AI Data Gateway

                         AI Agent
                            │
                            ▼
                      MCP Gateway
                            │
                 ┌──────────┴──────────┐
                 │                     │
             Identity              Authorization
                 │                     │
                 └──────────┬──────────┘
                            │
                     Connection Layer
                            │
             ┌──────────────┼──────────────┐
             ▼              ▼              ▼
          GitHub          Notion       Google Drive
             │              │              │
             └──────────────┼──────────────┘
                            │
                       Private Data
