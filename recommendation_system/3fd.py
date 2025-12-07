import json
import random

# 1. Define the specific Low-Level & Engineering Skills
skills = [
    "C++", "CPP", "C Plus Plus", "Modern C++", "C++11", "C++14", "C++17",
    "C", "Embedded C", "Objective-C",
    "Verilog", "SystemVerilog", "VHDL", "SystemC",
    "Assembly", "ASM", "ARM Assembly", "x86 Assembly", "MIPS Assembly",
    "Rust", "Go", "Golang",
    "Matlab", "Simulink", "LabVIEW",
    "Lua", "Perl", "Tcl", "Bash", "Shell Scripting", "PowerShell",
    "Python", "MicroPython", "CircuitPython",
    "Ada", "Fortran", "Pascal", "COBOL",
    "Lisp", "Haskell", "Erlang", "Elixir", "Ocaml",
    "RTOS", "FreeRTOS", "Device Drivers", "Firmware"
]

# 2. Define Templates to vary the sentence structure
# {skill} is the placeholder where the language will be inserted
templates = [
    "We are looking for a developer proficient in {skill}.",
    "Strong knowledge of {skill} is required for this embedded role.",
    "The candidate must have experience with {skill} programming.",
    "Our firmware is entirely written in {skill}.",
    "He has 5 years of experience in {skill} development.",
    "Experience in {skill} is a huge plus.",
    "The project involves writing low-latency code in {skill}.",
    "She optimized the legacy {skill} codebase.",
    "We need someone to debug {skill} modules.",
    "Can you write a compiler using {skill}?",
    "The hardware simulation was done using {skill}.",
    "Proficiency in {skill} and linear algebra is needed.",
    "The kernel module is implemented in {skill}.",
    "We are migrating our system from C to {skill}.",
    "Knowledge of hardware description languages like {skill} is essential.",
    "The algorithm requires a robust implementation in {skill}.",
    "This role focuses on {skill} for signal processing.",
    "You will be working with {skill} on a daily basis.",
    "The backend logic relies on high-performance {skill}.",
    "Understanding of memory management in {skill} is critical."
]

training_data = []

# 3. Generate 1000 samples
for _ in range(1000):
    skill = random.choice(skills)
    template = random.choice(templates)
    
    # Create the text
    text = template.format(skill=skill)
    
    # Calculate EXACT indices
    start_index = text.find(skill)
    end_index = start_index + len(skill)
    
    # Verify alignment (sanity check)
    if text[start_index:end_index] != skill:
        print(f"Error alignment for: {text}")
        continue

    # Construct spaCy format
    annotation = {
        "entities": [
            [start_index, end_index, "SKILL"]
        ]
    }
    
    training_data.append([text, annotation])

# 4. Save to file
with open("third_part.json", "w", encoding="utf-8") as f:
    json.dump(training_data, f, indent=2)

print(f"Successfully generated {len(training_data)} samples to 'training_data.json'")