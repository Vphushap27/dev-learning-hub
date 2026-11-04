#!/usr/bin/env python3
"""Dev Learning Hub CLI.

python run.py list
python run.py run binary_search
python run.py run all
python run.py roadmap dsa
"""
import argparse
import importlib
import pathlib
import sys

ROOT = pathlib.Path(__file__).parent
DEMOS = {
    "binary_search": "algorithms.binary_search",
    "sorting": "algorithms.sorting",
    "graphs": "algorithms.graphs",
    "dp": "algorithms.dynamic_programming",
    "lru_cache": "algorithms.lru_cache",
    "rate_limiter": "system_design.rate_limiter",
    "url_shortener": "system_design.url_shortener",
    "consistent_hashing": "system_design.consistent_hashing",
}


def run_demo(name):
    print(f"\n=== {name} ===")
    importlib.import_module(DEMOS[name]).demo()


def main():
    p = argparse.ArgumentParser(description="Dev Learning Hub")
    sub = p.add_subparsers(dest="cmd", required=True)
    sub.add_parser("list", help="sab demos/roadmaps dikhao")
    r = sub.add_parser("run", help="demo chalao")
    r.add_argument("name", choices=list(DEMOS) + ["all"])
    m = sub.add_parser("roadmap", help="roadmap padho")
    m.add_argument("name", choices=[f.stem for f in (ROOT / "roadmaps").glob("*.md")])
    a = p.parse_args()

    if a.cmd == "list":
        print("Demos   :", ", ".join(DEMOS))
        print("Roadmaps:", ", ".join(sorted(f.stem for f in (ROOT / "roadmaps").glob("*.md"))))
    elif a.cmd == "run":
        for n in (DEMOS if a.name == "all" else [a.name]):
            run_demo(n)
    else:
        print((ROOT / "roadmaps" / f"{a.name}.md").read_text())


if __name__ == "__main__":
    sys.exit(main())
