<div align="center">
  <img src="assets/banner.png" alt="DonMorpheus — whoami" width="100%" />
</div>

<p align="center">
  <strong>Adversary simulation / red team</strong> · authorized labs<br/>
  Windows · Linux · Active Directory · C2 as a detection problem
</p>

<p align="center">
  <a href="https://github.com/DonMorpheus/fieldnotes">fieldnotes</a>
  ·
  <a href="https://github.com/DonMorpheus/loaders">loaders</a>
  ·
  <a href="https://github.com/DonMorpheus/havoc-hiddendesktop">havoc-hiddendesktop</a>
  ·
  <a href="https://github.com/DonMorpheus/ctf-toolkit">ctf-toolkit</a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/lab-authorized-9b2d22?style=flat-square&labelColor=1c1612" alt="authorized lab"/>
  <img src="https://img.shields.io/badge/scope-Windows%20%7C%20Linux%20%7C%20AD-c44536?style=flat-square&labelColor=1c1612" alt="scope"/>
  <img src="https://img.shields.io/badge/open%20to-work-ead9c4?style=flat-square&labelColor=1c1612" alt="open to work"/>
</p>

---

### whoami

Operator in authorized labs (own VMs, HTB, GOAD-style forests). I run the chain, then write it down so **blue can hunt it** — leftover artifacts, telemetry, mitigations. Not a blog. Not a highlight reel.

> Operator labu. Red team. Notatki tak, żeby dało się z nich polować — nie tylko odtwarzać atak.

---

### Selected work

| Repo | What a recruiter is looking at |
|------|--------------------------------|
| **[fieldnotes](https://github.com/DonMorpheus/fieldnotes)** | Public lab manual. Kill-chain notes the way an operator actually used them: steps, leftovers, what blue still sees. |
| **[loaders](https://github.com/DonMorpheus/loaders)** | Lab loaders and persist in C: Early Bird APC, COM TreatAs / ClickOnce (`T1546.015`), Linux eBPF implant (`T1547.006`). |
| **[havoc-hiddendesktop](https://github.com/DonMorpheus/havoc-hiddendesktop)** | Working Havoc port of HiddenDesktop (HVNC). Stock BOF dies on CoffeeLdr / inject / rportfwd — this tree runs. |
| **[ctf-toolkit](https://github.com/DonMorpheus/ctf-toolkit)** | HTB / lab scripts from real boxes. Machine-specific. No flags, no VPN configs, no live creds. |

---

### How I work

- **Lab first.** If I did not run it, the note says `RESEARCH`. If I did, it says `LAB`.
- **Detection in the same breath.** Size vs the real binary, what lands on disk, what `ss` still leaks, which Event IDs fire.
- **No live C2, no client data, no flags in git.** Public code is for labs you own or have written permission to test.

```text
$ echo $FOCUS
Windows internals · Linux persist · AD assumed-breach · operator tooling

$ echo $OPEN_TO
red team  ·  adversary simulation  ·  detection engineering  ·  pentest
```

---

### Stack I actually use

C · Python · Bash · Windows COM / APC · eBPF · AD (Kerberos trails, assumed-breach) · operator-side C2 modules (Havoc)

Hands gym: Hack The Box (Linux, Windows, AD) plus home lab VMs.

---

<p align="center">
  <sub>Authorized lab &amp; security research only. Not a license to attack systems you do not own.</sub><br/>
  <sub>Reach me on GitHub — profile marked <strong>available for hire</strong>.</sub>
</p>
