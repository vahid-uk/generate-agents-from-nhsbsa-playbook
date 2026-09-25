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