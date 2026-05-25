# Password Hunter Game (Cazador de Contraseñas)

An interactive terminal-based game developed in Python that challenges players to act as a **Password Hunter**. The core objective is to generate and strictly validate secure, non-repeating random passwords to unlock mysterious chests, accumulate points, and handle critical system errors seamlessly.

This project was built to satisfy the academic requirements for **Phase 5 of the Programming Logic course** (Systems Engineering Program - Third Semester) at **UNAD** (Universidad Nacional Abierta y a Distancia).

---

##  Software Engineering Core Principles Applied

This application avoids monolithic procedural code by strictly leveraging **Clean Code** principles and the **Object-Oriented Programming (OOP)** paradigm:

* **Encapsulation:** The `Contrasena` class completely self-contains its strict validation rules, data states, and cryptographic character sets.
* **Inheritance & Polymorphism:** A base `Cofre` abstract-like structure defines the chest blueprint. Distinct sub-classes (`CofreComun`, `CofreRaro`, `CofreLegendario`, and `CofreMaldito`) override point allocation through behavioral polymorphism when opened.
* **Custom Exception Architecture:** Implements a robust hierarchy of user-defined exceptions (`LongitudInvalidaError`, `TipoDatoInvalidoError`, `ContrasenaInvalidaError`) ensuring the software never crashes due to faulty user inputs.
* **True Randomization:** Utilizes non-predictable sampling algorithms to guarantee that mandatory criteria (uppercase, lowercase, digits, and special characters) are scattered randomly without fixed patterns.

---

##  Strict Password Criteria

To successfully open a reward chest, every generated password must adhere to the following architectural constraints:
1.  **Minimum Length:** At least 8 characters (defined dynamically by the user).
2.  **No Duplicates:** Absolute constraint; zero repeated characters are allowed in the sequence.
3.  **Character Heterogeneity:** Must contain at least:
    * 1 Uppercase Letter (`A-Z`)
    * 1 Lowercase Letter (`a-z`)
    * 1 Digit (`0-9`)
    * 1 Allowed Special Character from this strict alphabet: `¿¡?=)(/¨*+-%&$#!.`

---

##  Reward System & Chest Mechanics

| Chest Type | Spawn Condition | Score Impact |
| :--- | :--- | :--- |
| **Común ** | Randomly chosen on valid password | `+10 Points` |
| **Raro ** | Randomly chosen on valid password | `+25 Points` |
| **Legendario ** | Randomly chosen on valid password | `+50 Points` |
| **Maldito ** | Triggered when password integrity fails | `-20 Points` |

---
