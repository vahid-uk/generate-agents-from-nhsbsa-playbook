## Shell script (basic content)

```
chmod +x create-nhsbsa-agents.sh
./create-nhsbsa-agents.sh
```

## Python script (a bit more sophisticated)

The python script should produce a details version of agents and skills for the NHSBSA project. It should include the following features:

python3 -m pip install requests beautifulsoup4

python3 build-nhsbsa-agents.py

It will produce:
```
nhsbsa-playbook-agents/
├── AGENTS.md
├── PLAYBOOK.md
├── SOURCES.md
├── VERSION.md
└── skills/
├── apis/
│   ├── SKILL.md
│   └── references.md
├── coding/
├── content-security-policy/
├── frontends/
├── git/
├── git-history-rewrite/
├── java/
├── licensing/
├── logging/
├── naming-conventions/
├── nodejs/
├── patching/
├── peer-review/
├── personal-data/
├── readmes/
├── release-adoption/
├── repository-files/
├── secrets-detection/
├── secure-development/
├── security-headers/
├── static-analysis/
├── style-guides/
├── technologies/
└── testing/
```

and, importantly:
```
nhsbsa-playbook-agents.zip
```



## Python script with local ollama instance (detailed content)

```
- python3 -m pip install requests beautifulsoup4
- ollama pull qwen3:14b
  Then exit with /bye.
```

3. Run the complete pipeline
   Once Ollama is running:

ollama serve

In another terminal:

python3 build-nhsbsa-agents-with-qwen3.py --model qwen3:14b

For the first run, I'd actually use:

```
python3 build-nhsbsa-agents-with-qwen3.py \
--model qwen3:14b \
--max-pages 300 \
--output ./nhsbsa-build
```

You'll get:

```
nhsbsa-build/
├── nhsbsa-playbook-agents/
│   ├── AGENTS.md
│   ├── PLAYBOOK.md
│   ├── SOURCES.md
│   ├── VERSION.md
│   ├── GENERATION.json
│   │
│   ├── source/
│   │   ├── 001-....md
│   │   ├── 002-....md
│   │   └── ...
│   │
│   └── skills/
│       ├── apis/
│       │   ├── SKILL.md
│       │   └── references.md
│       ├── coding/
│       ├── content-security-policy/
│       ├── frontends/
│       ├── git/
│       ├── git-history-rewrite/
│       ├── java/
│       ├── licensing/
│       ├── logging/
│       ├── naming-conventions/
│       ├── nodejs/
│       ├── patching/
│       ├── peer-review/
│       ├── personal-data/
│       ├── readmes/
│       ├── release-adoption/
│       ├── repository-files/
│       ├── secrets-detection/
│       ├── secure-development/
│       ├── security-headers/
│       ├── static-analysis/
│       ├── style-guides/
│       ├── technologies/
│       └── testing/
│
└── nhsbsa-playbook-agents.zip
```
4. Why this version is substantially better
   The important difference is that the LLM gets the actual structured content of each source page:

HEADINGS
+
PARAGRAPHS
+
LISTS
+
TABLES
+
CODE BLOCKS
+
SOURCE URL

rather than merely receiving the page title and a list of headings.

The generation prompt then forces the model to turn that into operational
agent guidance rather than a generic summary.

For example, an agent encountering a dependency change should be able to
follow:

```
dependency change
│
├── patching skill
│       │
│       ├── dependency declaration
│       ├── vulnerability handling
│       └── package manager
│
└── release-adoption skill
│
├── current release status
├── adoption stage
└── migration implications
```

rather than simply being told "keep dependencies up to date."

5. One thing I'd strongly recommend
   For the first generation, use a reasonably capable model rather than the
   smallest Ollama model available. This is a documentation synthesis task, and
   the distinction between:

"NHSBSA recommends X"

and

"NHSBSA requires X unless Y"

is important.

If your machine can handle it, use a larger Qwen model available through
Ollama. The script's --model option means you don't have to change the
code:


python3 build-nhsbsa-agents-with-qwen3.py --model <your-model>

The generated GENERATION.json will record exactly which model produced the
pack.

One further improvement I'd make after the first run
I'd run a second LLM validation pass over the generated skills, comparing
each SKILL.md against its original source pages and asking the model to
identify:

invented requirements

lost requirements

changed thresholds

missing exceptions

incorrect MUST/SHOULD distinctions

unsupported claims

missing source references

That gives you:

```
crawl
↓
LLM extraction
↓
SKILL.md
↓
LLM source-fidelity review
↓
corrected SKILL.md
↓
ZIP
```

For something intended to guide production coding agents, that second pass is worth doing. It reduces the risk of the local knowledge pack gradually becoming an inaccurate interpretation of the NHSBSA source.

---

## How to run it
Install the dependencies:

```
python3 -m pip install requests beautifulsoup4
```

Install/start Ollama and pull the model:

```
ollama pull qwen3:14b
ollama serve
```

Then:

```
python3 build-nhs-agent-knowledge.py \
--model qwen3:14b \
--max-pages 500 \
--output ./nhs-agent-build \
--force
```

The resulting archive will be:

./nhs-agent-build/nhs-agent-knowledge.zip

What I specifically changed from the previous script
The important addition is the llms.txt discovery layer.

Conceptually the crawler now does:
```
                    NHS source
                       │
              ┌────────┴────────┐
              │                 │
           llms.txt           HTML
              │                 │
              ▼                 ▼
       curated links       page links
              │                 │
              └────────┬────────┘
                       ▼
                relevant pages
                       │
                       ▼
                Markdown version
                where available
                       │
                       ▼
                 source model
                       │
                       ▼
                  LLM synthesis
                       │
          ┌────────────┼─────────────┐
          ▼            ▼             ▼
       MUST/SHOULD     DO/DON'T     Sources
          │            │             │
          └────────────┼─────────────┘
                       ▼
                    SKILL.md
```

This follows the current llms.txt v2 approach rather than treating llms.txt as a giant replacement for the documentation. The specification explicitly describes llms.txt as a concise guide that points agents toward detailed material, and v2 also supports scoped files and Markdown page representations.
L
llms-txt
+1

The NHS Service Manual side is deliberately broader than just components
The crawler starts at the design system and follows its subsequent links, so it can capture:

design principles

styles

components

patterns

prototyping

production implementation

accessibility-related guidance

component-specific usage

pattern-specific usage

explicit Do/Don't material

That's important because the Service Manual describes components as reusable UI elements and patterns as tested solutions to common needs, so simply dumping component names into an agent context wouldn't give the agent enough information to make appropriate implementation decisions.
N
nhs.uk
+1

For example, the generated components/SKILL.md should be able to tell an agent not just what a component is, but preserve the source's:

when to use
+
when not to use
+
implementation
+
accessibility
+
Do
+
Don't

That distinction matters particularly for the NHS Service Manual's explicit Do/Don't guidance, where the guidance can include accessibility-specific reasons for a particular implementation choice.
N
nhs.uk

One important refinement I'd make
I would not make the generated AGENTS.md contain all of the NHS guidance itself.

Keep it as the agent's routing layer:
```
AGENTS.md
│
├── "I'm changing backend code"
│          ↓
│      coding
│      secure-development
│      testing
│
├── "I'm changing a form"
│          ↓
│      design-system
│      components
│      forms
│      accessibility
│      content
│
├── "I'm adding a new interaction"
│          ↓
│      patterns
│      components
│      accessibility
│
└── "I'm changing NHS frontend code"
↓
production-frontend
design-system
components
accessibility
```

That keeps the root context small while allowing the agent to load detailed guidance only when relevant.

It also reflects the purpose of llms.txt: a concise navigational layer followed by detailed material when the agent actually needs it.
L
llms-txt

One other useful source relationship is that the Service Manual's current guidance explicitly says to build on common NHS styles, patterns and components, and to share new components or patterns rather than solving the same problem independently.
N
nhs.uk
The generated design-system, components and patterns skills should therefore reinforce that relationship rather than treating the design system as merely a collection of CSS components.