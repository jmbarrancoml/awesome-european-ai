# Contributing to Awesome European AI

Thanks for your interest in contributing!

## Guidelines

### What belongs here

- Companies incorporated or headquartered in Europe
- Open source projects owned by a European company, or run by European maintainers
- Resources specifically relevant to the European AI ecosystem

### What doesn't belong

- Companies incorporated outside Europe. European founders, a European office or
  European datacentres are not enough on their own: the entity itself has to be
  European. Hugging Face (Delaware, HQ in New York) is the usual borderline case
- Companies with no European presence
- Generic AI tools/resources better suited to global awesome lists
- Discontinued projects or defunct companies

### Evidence

Country claims should be checkable. A company register entry, a VAT number or an
imprint on the official site all work. If the only public statement is "European
company" with no entity behind it, the entry gets the 🇪🇺 EU flag instead of a
national one.

### Keep the data files in sync

Every README entry has a matching object in `data/`: companies go in
`data/companies.json`, projects in `data/open-source.json`, everything else in
`data/resources.json` or `data/research-labs.json`. Add both, in the same
position, or the pull request is incomplete.

Run `python3 scripts/check-sync.py` before opening the pull request. It compares
every README table against its JSON file and names whatever is missing.

## How to contribute

1. Fork this repository
2. Add your suggestion to the appropriate section
3. Follow the existing format (table structure, country flags, descriptions)
4. Submit a pull request

## Format

For companies:
```
| [Company Name](https://url.com) | 🇩🇪 Country | Focus area | Brief description |
```

For open source projects:
```
| [Project Name](https://github.com/...) | 🇩🇪 Country | Brief description |
```

## Country flags

Use emoji flags: 🇫🇷 🇩🇪 🇬🇧 🇳🇱 🇪🇸 🇮🇹 🇸🇪 🇨🇭 🇦🇹 🇧🇪 🇵🇱 🇮🇪 🇩🇰 🇫🇮 🇳🇴 🇵🇹 🇨🇿 🇱🇻 🇱🇹 🇪🇪 🇧🇬 🇷🇴 🇭🇺 🇬🇷 🇱🇺 🇸🇮 🇸🇰 🇭🇷 🇪🇺

## Questions?

Open an issue if you're unsure about anything.
