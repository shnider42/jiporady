from flask import Flask, jsonify, render_template, request
import os
import random

app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False
app.secret_key = os.environ.get("SECRET_KEY", "dev-only-secret-key")

GAME_DATA = {'title': 'Jiporady: Cybersecurity',
 'subtitle': 'From password hygiene and scam spotting to protocols, cryptography, and incident lore',
 'rounds': {'round_1': {'name': 'Round 1',
                        'categories': [{'title': 'Lock It Down',
                                        'clues': [{'value': 100,
                                                   'question': 'Fingerprint and face scans belong to this broad identity-checking method.',
                                                   'answer': 'Biometric authentication'},
                                                  {'value': 200,
                                                   'question': 'Requiring two independent proofs before entry is commonly shortened to these three letters.',
                                                   'answer': 'MFA'},
                                                  {'value': 300,
                                                   'question': 'A browser padlock usually signals this encrypted website protocol.',
                                                   'answer': 'HTTPS'},
                                                  {'value': 400,
                                                   'question': 'This vaulting application creates and stores unique login secrets for many accounts.',
                                                   'answer': 'Password manager'},
                                                  {'value': 500,
                                                   'question': 'Installing vendor fixes promptly and consistently is formalized under this defensive practice.',
                                                   'answer': 'Patch management'}]},
                                       {'title': 'Scam School',
                                        'clues': [{'value': 100,
                                                   'question': 'A fake message crafted to steal credentials belongs to this familiar attack type.',
                                                   'answer': 'Phishing'},
                                                  {'value': 200,
                                                   'question': 'Urgency, fear, and perceived rank are favorite tools in this people-focused manipulation field.',
                                                   'answer': 'Social engineering'},
                                                  {'value': 300,
                                                   'question': 'Email bait aimed specifically at senior executives uses this ocean-sized nickname.',
                                                   'answer': 'Whaling'},
                                                  {'value': 400,
                                                   'question': 'Fraudulent texts sent to phones are known by this blended term.',
                                                   'answer': 'Smishing'},
                                                  {'value': 500,
                                                   'question': 'An impersonating phone call from a supposed bank or agency fits this voice-based label.',
                                                   'answer': 'Vishing'}]},
                                       {'title': 'Cyber Zoo',
                                        'clues': [{'value': 100,
                                                   'question': 'Named after a wooden Greek gift, a malicious program pretends to be useful.',
                                                   'answer': 'Trojan horse'},
                                                  {'value': 200,
                                                   'question': 'This self-replicating threat spreads between systems without attaching itself to another file.',
                                                   'answer': 'Computer worm'},
                                                  {'value': 300,
                                                   'question': 'Researchers use this sweet-sounding decoy as bait for intruders.',
                                                   'answer': 'Honeypot'},
                                                  {'value': 400,
                                                   'question': 'A hidden collection of compromised devices controlled together has this robotic-sounding name.',
                                                   'answer': 'Botnet'},
                                                  {'value': 500,
                                                   'question': 'Software that secretly records every keystroke carries this straightforward label.',
                                                   'answer': 'Keylogger'}]},
                                       {'title': 'Pop Culture Mainframes',
                                        'clues': [{'value': 100,
                                                   'question': 'In WarGames, a teenager nearly triggers global disaster after connecting to this military supercomputer.',
                                                   'answer': 'WOPR'},
                                                  {'value': 200,
                                                   'question': 'Neo follows a white rabbit before learning reality is simulated in this 1999 movie.',
                                                   'answer': 'The Matrix'},
                                                  {'value': 300,
                                                   'question': "Mr. Robot's hooded protagonist narrates his fractured world under this first name.",
                                                   'answer': 'Elliot'},
                                                  {'value': 400,
                                                   'question': "Jurassic Park's disaster worsens after this disgruntled programmer disables crucial systems.",
                                                   'answer': 'Dennis Nedry'},
                                                  {'value': 500,
                                                   'question': 'In Sneakers, the code-breaking device depends on a breakthrough from this mathematical branch.',
                                                   'answer': 'Number theory'}]},
                                       {'title': 'Home Network Hangout',
                                        'clues': [{'value': 100,
                                                   'question': 'The household box directing traffic among local devices and the wider internet.',
                                                   'answer': 'Router'},
                                                  {'value': 200,
                                                   'question': "A wireless network's public-facing identifier is abbreviated with these four letters.",
                                                   'answer': 'SSID'},
                                                  {'value': 300,
                                                   'question': 'Keeping visitors on an isolated guest setup demonstrates this architectural practice.',
                                                   'answer': 'Network segmentation'},
                                                  {'value': 400,
                                                   'question': 'Disabling this one-button pairing feature removes a commonly abused convenience.',
                                                   'answer': 'WPS'},
                                                  {'value': 500,
                                                   'question': 'A resolver translates human-readable site names into numeric addresses through this system.',
                                                   'answer': 'DNS'}]},
                                       {'title': 'Humans Are Complicated',
                                        'clues': [{'value': 100,
                                                   'question': 'Holding a secured door for an unknown person can enable this piggybacking tactic.',
                                                   'answer': 'Tailgating'},
                                                  {'value': 200,
                                                   'question': 'Watching a nearby screen or keypad to capture a secret fits this observational technique.',
                                                   'answer': 'Shoulder surfing'},
                                                  {'value': 300,
                                                   'question': 'Searching discarded paperwork for useful details has this trash-themed nickname.',
                                                   'answer': 'Dumpster diving'},
                                                  {'value': 400,
                                                   'question': 'A convincing badge may exploit our tendency to obey perceived rank, known by this persuasion principle.',
                                                   'answer': 'Authority'},
                                                  {'value': 500,
                                                   'question': 'Leaving infected removable media in a parking lot relies on curiosity and carries this lure-based name.',
                                                   'answer': 'Baiting'}]}]},
            'round_2': {'name': 'Double Jiporady',
                        'categories': [{'title': 'Acronym Gauntlet',
                                        'clues': [{'value': 200,
                                                   'question': 'A central platform aggregating logs and raising alerts is known by these four letters.',
                                                   'answer': 'SIEM'},
                                                  {'value': 400,
                                                   'question': 'The industry scoring system rating software flaws from low to critical uses this abbreviation.',
                                                   'answer': 'CVSS'},
                                                  {'value': 600,
                                                   'question': 'A public identifier assigned to a disclosed vulnerability begins with this three-letter prefix.',
                                                   'answer': 'CVE'},
                                                  {'value': 800,
                                                   'question': 'Policies combining user, resource, and context properties rather than relying only on roles follow this model.',
                                                   'answer': 'ABAC'},
                                                  {'value': 1000,
                                                   'question': 'Enterprise single sign-on often uses this protocol to pass identity assertions between separate organizations.',
                                                   'answer': 'SAML'}]},
                                       {'title': 'Web App Woes',
                                        'clues': [{'value': 200,
                                                   'question': 'Untrusted input changes a database command, producing this classic flaw.',
                                                   'answer': 'SQL injection'},
                                                  {'value': 400,
                                                   'question': 'A browser executes attacker-supplied code because output was not safely handled.',
                                                   'answer': 'Cross-site scripting'},
                                                  {'value': 600,
                                                   'question': "A logged-in user's browser is tricked into performing an unwanted action on another page.",
                                                   'answer': 'Cross-site request forgery'},
                                                  {'value': 800,
                                                   'question': 'An application fetches a remote location chosen by an attacker, potentially reaching internal services.',
                                                   'answer': 'Server-side request forgery'},
                                                  {'value': 1000,
                                                   'question': "Unsafe assumptions about object references let one customer expose another person's records under this OWASP category.",
                                                   'answer': 'Broken access control'}]},
                                       {'title': 'Crypto Cabinet',
                                        'clues': [{'value': 200,
                                                   'question': 'Adding random data before hashing makes identical secrets produce different outputs.',
                                                   'answer': 'Salt'},
                                                  {'value': 400,
                                                   'question': 'One key locks data while a mathematically related partner unlocks it.',
                                                   'answer': 'Asymmetric cryptography'},
                                                  {'value': 600,
                                                   'question': 'This operation proves integrity and origin through a private signing key.',
                                                   'answer': 'Digital signature'},
                                                  {'value': 800,
                                                   'question': 'A deliberately slow, memory-intensive function helps protect stored credentials against guessing.',
                                                   'answer': 'Password hashing'},
                                                  {'value': 1000,
                                                   'question': 'Past sessions remain safe even when a long-term private key is later exposed because of this property.',
                                                   'answer': 'Perfect forward secrecy'}]},
                                       {'title': 'Blue Team Bench',
                                        'clues': [{'value': 200,
                                                   'question': 'A decoy file or credential triggers an alert whenever someone touches it.',
                                                   'answer': 'Canary token'},
                                                  {'value': 400,
                                                   'question': 'A host-based product watches processes, files, and behavior for malicious activity, abbreviated by these letters.',
                                                   'answer': 'EDR'},
                                                  {'value': 600,
                                                   'question': 'Tactics and techniques carrying identifiers such as T1059 are organized by this framework.',
                                                   'answer': 'MITRE ATT&CK'},
                                                  {'value': 800,
                                                   'question': 'A chronological record linking evidence to every handler preserves this legal concept.',
                                                   'answer': 'Chain of custody'},
                                                  {'value': 1000,
                                                   'question': 'Memory, active connections, and running processes disappear after shutdown, so responders prioritize them under this collection principle.',
                                                   'answer': 'Order of volatility'}]},
                                       {'title': 'Protocol Deep Cuts',
                                        'clues': [{'value': 200,
                                                   'question': 'Secure remote-shell service normally listens on TCP port 22.',
                                                   'answer': 'SSH'},
                                                  {'value': 400,
                                                   'question': "A ticket-granting system widely used in Windows domains takes its name from Greek mythology's three-headed guard dog.",
                                                   'answer': 'Kerberos'},
                                                  {'value': 600,
                                                   'question': 'A browser policy instructing clients to keep using encrypted connections for a specified period.',
                                                   'answer': 'HSTS'},
                                                  {'value': 800,
                                                   'question': 'Cryptographic signatures added to name-resolution records and zones provide this extension.',
                                                   'answer': 'DNSSEC'},
                                                  {'value': 1000,
                                                   'question': 'Built over UDP and used by HTTP/3, this modern transport has a four-letter name.',
                                                   'answer': 'QUIC'}]},
                                       {'title': 'Infamous but Educational',
                                        'clues': [{'value': 200,
                                                   'question': 'A 1988 self-spreading program written by a Cornell graduate student became one of the earliest major internet outbreaks.',
                                                   'answer': 'Morris worm'},
                                                  {'value': 400,
                                                   'question': 'A 2017 extortion outbreak used the leaked EternalBlue exploit and displayed a red countdown.',
                                                   'answer': 'WannaCry'},
                                                  {'value': 600,
                                                   'question': 'The supply-chain compromise discovered in 2020 reached organizations through tampered Orion updates.',
                                                   'answer': 'SolarWinds'},
                                                  {'value': 800,
                                                   'question': 'Industrial sabotage malware damaged Iranian centrifuges by manipulating programmable logic controllers.',
                                                   'answer': 'Stuxnet'},
                                                  {'value': 1000,
                                                   'question': 'A missing bounds check in OpenSSL exposed server memory in 2014 and inspired a bleeding-heart logo.',
                                                   'answer': 'Heartbleed'}]}]}},
 'final': {'category': 'Final Jiporady: Cryptographic History',
           'question': "A landmark 1976 method lets two parties establish shared material over an observable channel without any prior secret; its creators' surnames also name the protocol.",
           'answer': 'Diffie-Hellman key exchange'}}


def all_categories():
    categories = []
    for round_data in GAME_DATA["rounds"].values():
        for category in round_data["categories"]:
            categories.append(
                {
                    "category": category["title"],
                    "clues": category["clues"],
                }
            )
    return categories


def build_board(category_count=6):
    categories = all_categories()
    category_count = max(4, min(category_count, len(categories)))
    return random.sample(categories, category_count)


def build_stats():
    categories = all_categories()
    return {
        "total_categories": len(categories),
        "total_clues": sum(len(category["clues"]) for category in categories),
    }


@app.route("/")
def index():
    category_count = request.args.get("categories", default=6, type=int) or 6
    initial_board = build_board(category_count)
    return render_template(
        "index.html",
        title=GAME_DATA["title"],
        subtitle=GAME_DATA["subtitle"],
        stats=build_stats(),
        category_count=category_count,
        initial_board=initial_board,
    )


@app.route("/api/board")
def api_board():
    category_count = request.args.get("categories", default=6, type=int) or 6
    return jsonify({"board": build_board(category_count)})


@app.route("/api/game")
def game_data():
    return jsonify(GAME_DATA)


@app.route("/health")
def health_check():
    return {"ok": True, "app": "jiporady-cybersecurity"}


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
