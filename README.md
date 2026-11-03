# 🚀 Programming Core Journey: Python, SQL & First Principles

Welcome to your personal learning sanctuary. This repository is not just about learning *syntax* (the "how"), but about mastering *programming principles* (the "why"). 

## 📌 The Philosophy
Instead of learning a language in a vacuum, we approach programming as a set of universal concepts. Python and SQL are our tools to implement these concepts.

## 🗺️ Learning Roadmap

### 🟢 Module 1: Algorithmic Thinking & Basics
- **Python**: Basic types, loops, conditionals.
- **SQL**: Basic SELECT, WHERE, and JOINs.
- **Core Principle**: **Time & Space Complexity (Big O)**. Learn why one solution is "better" than another.
- [ ] Progress: 0%

### 🔵 Module 2: Data Architecture
- **Python**: Advanced collections (Dictionaries, Sets, Tuples).
- **SQL**: Normalization (1NF, 2NF, 3NF), Primary/Foreign Keys.
- **Core Principle**: **Data Modeling**. How to structure information for efficiency and integrity.
- [ ] Progress: 0%

### 🟡 Module 3: Modularity & Clean Code
- **Python**: Functions, Modules, and Type Hinting.
- **SQL**: Views and Common Table Expressions (CTEs).
- **Core Principle**: **DRY (Don't Repeat Yourself)**. Reducing redundancy to make code maintainable.
- [ ] Progress: 0%

### 🟠 Module 4: State & Object Orientation
- **Python**: Classes, Inheritance, and Mixins.
- **SQL**: Transactions and ACID properties.
- **Core Principle**: **Encapsulation & Abstraction**. Hiding complexity and managing state.
- [ ] Progress: 0%

### 🔴 Module 5: System Integration
- **Python**: Database connectivity (sqlite3), API basics, Error Handling.
- **SQL**: Window Functions, Indexing strategies.
- **Core Principle**: **Separation of Concerns**. Keeping your data, logic, and presentation layers distinct.
- [ ] Progress: 0%

## 🛠️ Repository Structure

```
📁 curriculum/
   ├── module-1/
   │   ├── 1-1-basics.md          # Variables, types, I/O
   │   ├── 1-2-control-flow.md    # if/elif/else, loops
   │   └── 1-3-big-o.md           # Big O notation & analysis
   ├── module-2/                  # Data structures & DB design
   ├── module-3/                  # Functions, modules & DRY
   ├── module-4/                  # Classes & OOP
   └── module-5/                  # System integration

📁 python/
   ├── module-1/exercises/        # Practice problems with starters
   │   ├── 1-1-max-value/
   │   ├── 1-3-temperature-analyzer/
   │   └── ...
   └── module-1/solutions/        # Complete solutions (reference)

📁 sql/
   ├── module-1/exercises/        # Query practice with starters
   │   ├── 1-1-customer-orders/
   │   └── ...
   └── module-1/solutions/        # Complete solutions (reference)

📁 principles/                     # Deep-dive theory files
   ├── big-o-notation.md
   ├── data-modeling.md
   ├── dry-principle.md
   ├── encapsulation-abstraction.md
   └── separation-of-concerns.md

📁 projects/
   └── hello-world/               # Starter project template
```

## 📚 How to Use This Repository

### For Learners

1. **Start with Module 1:** Read `/curriculum/module-1/1-1-basics.md`
2. **Work through exercises:** Complete exercises in `/python/module-1/exercises/`
3. **Check your work:** Compare with solutions in `/python/module-1/solutions/`
4. **Deep dive:** Read principle files for theoretical understanding
5. **Progress:** Move to the next lesson when ready

### Lesson Structure

Each lesson includes:
- **Objectives** - What you'll learn
- **Concepts** - Explained with examples
- **Python focus** - Language-specific practice
- **SQL focus** - Database-specific practice
- **Exercises** - Hands-on problems
- **Complexity analysis** - Understanding performance

### Exercise Structure

Each exercise has:
- **problem.md** - Problem statement and requirements
- **starter.py/sql** - Template with TODOs to guide your work
- **solution.py/sql** - Complete working solution with explanations

## 🚀 Getting Started

**Option 1: Follow the curriculum sequentially**
```
1. Read: /curriculum/module-1/1-1-basics.md
2. Code: /python/module-1/exercises/1-1-max-value/
3. Learn: /principles/big-o-notation.md
```

**Option 2: Jump to a specific topic**
- Learning about data structures? → `/curriculum/module-2/`
- Want to understand classes? → `/curriculum/module-4/`
- Need complex queries? → `/curriculum/module-5/` (SQL section)

## 💡 Core Principles Covered

| Module | Principle | Why It Matters |
|---|---|---|
| 1 | **Big O Notation** | Write fast algorithms that scale |
| 2 | **Data Modeling** | Organize data efficiently and avoid redundancy |
| 3 | **DRY (Don't Repeat Yourself)** | Write maintainable code that's easy to update |
| 4 | **Encapsulation & Abstraction** | Hide complexity, manage state safely |
| 5 | **Separation of Concerns** | Build systems with independent, reusable parts |

## 📖 Reference Files

Quick reference for core concepts:
- `/principles/big-o-notation.md` - Algorithm efficiency (500+ lines with examples)
- `/principles/data-modeling.md` - Database design & normalization
- `/principles/dry-principle.md` - Code reuse patterns
- `/principles/encapsulation-abstraction.md` - OOP design
- `/principles/separation-of-concerns.md` - Layered architecture

## 🎯 Pro Tips

1. **Don't skip the principles** - They're the foundation for understanding "why"
2. **Solve exercises before checking solutions** - The struggle is where learning happens
3. **Analyze complexity** - Every exercise has a Big O analysis; understand it
4. **Build progressively** - Each module builds on previous concepts
5. **Test edge cases** - Always think about boundary conditions

## ❓ Common Questions

**Q: Should I use `max()` if Python has it?**
A: In real code, yes. In exercises, no—the goal is to understand *how* algorithms work.

**Q: Can I skip a module?**
A: Not recommended. Each module's principle underlies later concepts.

**Q: How long is this?**
A: ~20-30 hours total, depending on depth and practice.
