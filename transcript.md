# Transcript: Codex & MCP - Sharing for Scalability

## Introduction (Slide: Title - Codex and MCP: Sharing for Scalability)

"Welcome everyone! For today's lightning talk, I want to show how we can leverage the Model Context Protocol, or MCP, to make our AI agents more efficient. We'll use a festive 'Santa's Workshop Inventory' server I built to manage toy production."

---

## Case 1: The Inefficient Workshop (Separate Servers)

*(Slide: Subtitle - Case 1: Separate, Inefficient Servers)*

"In our first scenario, we are going to act like an old-school IT department. We believe in dedicated resources. We have 'Elf A' and 'Elf B', and each gets their very own, separate workshop server running on a different port."

*(Action: Open two server terminals. Server A runs on port 6274; Server B runs on port 6275.)*

"Now, let's have our two AI 'Elves' check the stock of 'Toy Trains'."

*(Action: Switch to two separate AI Client windows/consoles. User 1/Elf A types a prompt; User 2/Elf B types the same prompt.)*

**User 1 (Elf A Prompt):**
> `Hello, I am Elf A. Use the workshop tools to check the current stock of "Toy Train".`

**User 2 (Elf B Prompt):**
> `Hello, I am Elf B. Use the workshop tools to check the current stock of "Toy Train".`

*(AI response for both returns 'stock': 50)*

"Both elves report the stock is 50. Great. Now, Elf A is proactive and starts production."

**User 1 (Elf A Prompt):**
> `Use the "produce_toys" tool to make 10 more "Toy Train"s.`

*(Action: The Server A console prints "Elf workshop is producing..." and then the final status.)*

**Elf A (AI Response):**
> `Successfully produced 10 Toy Trains. New stock: 60`

*(Action: Immediately switch to User 2 (Elf B) and have them check stock again.)*

**User 2 (Elf B Prompt):**
> `Check the current stock of "Toy Train" again please.`

**Elf B (AI Response):**
> `Toy Train stock: 50`

*(Slide: Problem: Inconsistent Data & Resource Waste)*

"Uh oh. Elf B still thinks we only have 50 trains! Because they are connected to a completely separate server instance, our global inventory is inconsistent. We are also wasting system resources by running two full Python processes when one would suffice. This architecture is inefficient and unreliable."

---

## Case 2: The Efficient Workshop (Shared Server)

*(Action: Stop both server instances. Start a single instance of the server on port 6274.)*

*(Slide: Solution: Single Shared MCP Server)*

"Let's fix this with modern architecture. We shut down the redundant servers and fire up *one single, central workshop server* that both Elves will connect to."

*(Show Central Server terminal running on port 6274.)*

"Now we reconfigure both Elf A and Elf B to talk to this single source of truth."

*(Action: Switch to both AI Client windows. User 1/Elf A types a prompt; User 2/Elf B types the same prompt.)*

**User 1 (Elf A Prompt):**
> `Elf A reporting in. Use the workshop tools to check the current stock of "Toy Train".`

**User 2 (Elf B Prompt):**
> `Elf B reporting in. Use the workshop tools to check the current stock of "Toy Train".`

*(AI response for both correctly returns 'stock': 60 from the shared database.)*

"Perfect. Both Elves see the same, correct number now: 60."

"Now, let's try the concurrent production again. Elf A wants to make 5 dolls, and Elf B wants to make 10 teddy bears."

**User 1 (Elf A Prompt):**
> `Produce 5 "Doll"s using the produce_toys tool.`

**User 2 (Elf B Prompt):**
> `Produce 10 "Teddy Bear"s using the produce_toys tool.`

*(Action: Switch to the Central Server terminal. Both requests hit the single server instantly.)*


🎄 Starting Santa's Workshop Inventory MCP Server...
Elf workshop is producing 5 Dolls...
Elf workshop is producing 10 Teddy Bears...


*(Show AI responses once they complete.)*

**Elf A (AI Response):**
> `Successfully produced 5 Dolls. New stock: 205`

**Elf B (AI Response):**
> `Successfully produced 10 Teddy Bears. New stock: 110`

*(Slide: Summary: Efficiency and Consistency Achieved)*

"The single server instance handled both concurrent requests gracefully. It ensures data consistency and uses fewer system resources overall. By treating our MCP server as a shared, scalable service rather than a 1:1 client dependency, we achieve true efficiency in our AI-driven workshop."

"Thank you, and happy holidays!"
