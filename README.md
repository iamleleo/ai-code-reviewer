# AI Code Reviewer POC

## Objective

A system that automatically reviews code when developers create pull requests on GitHub.

## The Flow

1. Developer pushes code to GitHub and opens a pull request (PR).
2. GitHub sends us a notification (webhook).
3. Our system receives the notification.
4. AI agents examine the code looking for bugs, security issues, and style problems.
5. Our system posts comments back to the GitHub PR with findings.

```mermaid
graph TD
    subgraph External
        GH[GitHub]
    end

    subgraph API_Layer [Flask Backend]
        F[Flask Server]
        M[(MongoDB)]
        R[Redis Queue]
    end

    subgraph Processing_Layer [Worker Layer]
        C[Celery Worker]
        subgraph Agents [AI Orchestration]
            A1[Bug Detection Agent]
            A2[Security Agent]
            A3[Style Agent]
            A4[Performance Agent]
        end
    end

    %% Step 1: Webhook flow
    GH -->|1. Webhook: New PR| F
    F -->|Verify & Store| M
    F -->|Push Job| R
    F -.->|Fast Response 200 OK| GH

    %% Step 2: Async Processing
    R -->|2. Pick up Job| C
    C -->|Fetch Code| GH
    
    %% Step 3: Agentic Loop
    C -->|3. Parallel Calls| A1 & A2 & A3 & A4
    A1 & A2 & A3 & A4 -->|4. Results| C
    
    %% Step 4: Finalize
    C -->|Update Record| M
    C -->|5. Post Comments| GH
```
