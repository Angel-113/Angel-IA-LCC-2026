import copy
import yaml


def load_kb(filename):
    with open(filename, "r") as file:
        data = yaml.safe_load(file)

    facts = [tuple(f) for f in data.get("facts", [])]

    rules = []
    for r in data.get("rules", []):
        rule_id = r["id"]
        premises = [tuple(p) for p in r["if"]]
        conclusion = tuple(r["then"])
        rules.append((rule_id, premises, conclusion))

    return facts, rules


def is_var(v):
    return isinstance(v, str) and v[0].islower()


def unify(x, y, theta):
    if theta is None:
        return None
    if x == y:
        return theta
    if is_var(x):
        return unify_var(x, y, theta)
    if is_var(y):
        return unify_var(y, x, theta)
    if isinstance(x, tuple) and isinstance(y, tuple) and len(x) == len(y):
        return unify(x[1:], y[1:], unify(x[0], y[0], theta))
    return None


def unify_var(var, val, theta):
    if var in theta:
        return unify(theta[var], val, theta)
    if val in theta:
        return unify(var, theta[val], theta)
    theta[var] = val
    return theta


def substitute(term, theta):
    if isinstance(term, str):
        return theta.get(term, term) if is_var(term) else term
    return tuple(substitute(arg, theta) for arg in term)


def forward_chaining(query, base_facts, base_rules):
    kb = list(base_facts)
    new_atoms_order = []

    while True:
        new_in_round = []
        for rule_id, premises, conclusion in base_rules:
            thetas = [{}]
            for prem in premises:
                next_thetas = []
                for theta in thetas:
                    prem_sub = substitute(prem, theta)
                    for fact in kb:
                        th = unify(prem_sub, fact, copy.deepcopy(theta))
                        if th is not None:
                            next_thetas.append(th)
                thetas = next_thetas

            for theta in thetas:
                if not theta and premises:
                    continue
                new_fact = substitute(conclusion, theta)
                if new_fact not in kb and new_fact not in new_in_round:
                    new_in_round.append(new_fact)
                    new_atoms_order.append(new_fact)

        if not new_in_round:
            break
        kb.extend(new_in_round)

    proved = False
    for fact in kb:
        if unify(query, fact, {}) is not None:
            proved = True
            break

    return proved, new_atoms_order


rule_counter = 0


def rename_vars(rule):
    global rule_counter
    rule_counter += 1
    rid, prems, concl = rule

    def rn(term):
        return tuple(f"{arg}_{rule_counter}" if is_var(arg) else arg for arg in term)

    return rid, [rn(p) for p in prems], rn(concl)


def backward_chaining(goal, base_facts, base_rules):
    trace = []

    def bc_ask(q, theta, visited):
        q_sub = substitute(q, theta)
        if q_sub in visited:
            return

        for fact in base_facts:
            th = unify(q_sub, fact, copy.deepcopy(theta))
            if th is not None:
                trace.append(f"Hecho probado: {fact}")
                yield th

        for rule in base_rules:
            rid, prems, concl = rename_vars(rule)
            th = unify(q_sub, concl, copy.deepcopy(theta))
            if th is not None:
                trace.append(f"Abre regla {rid} para meta {q_sub}")
                for th2 in bc_and(prems, th, visited + [q_sub]):
                    yield th2

    def bc_and(goals, theta, visited):
        if not goals:
            yield theta
            return
        first, rest = goals[0], goals[1:]
        for th1 in bc_ask(first, theta, visited):
            for th2 in bc_and(rest, th1, visited):
                yield th2

    generator = bc_ask(goal, {}, [])
    try:
        next(generator)
        return True, trace
    except StopIteration:
        return False, trace


def main():
    facts, rules = load_kb("kb.yaml")

    queries = [
        ("AccesoNoche", "Ana"),
        ("AccesoNoche", "Luis"),
        ("AccesoNoche", "Marta"),
    ]

    print("--- ENCADENAMIENTO HACIA ADELANTE ---")
    for q in queries:
        proved, atoms = forward_chaining(q, facts, rules)
        print(f"Consulta {q}: {'PROBADA' if proved else 'NO PROBADA'}")
        if q == queries[0]:
            print(f"Átomos nuevos generados: {atoms}")

    print("\n--- ENCADENAMIENTO HACIA ATRÁS ---")
    for q in queries:
        global rule_counter
        rule_counter = 0
        proved, trace = backward_chaining(q, facts, rules)
        print(f"\nConsulta {q}: {'PROBADA' if proved else 'NO PROBADA'}")
        for step in trace:
            print("  ->", step)


if __name__ == "__main__":
    main()
