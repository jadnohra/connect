2020.05.06

What if we start from a universe?
The results look good, e.g

```
python -m ddq.demo.print_non_membership_definition
∀
├── x
└── ∀
    ├── y
    └── ⇔
        ├── ∈
        │   ├── x
        │   └── y
        └── ¬
            └── ∉
                ├── x
                └── y
```

However the building of the definition is still too noise

```
self._formula = (
            forall().set_binary(
                vars.put('x', universal_var()),
                forall().set_binary(
                    vars.put('y', universal_var()),
                    l_equiv().set_binary(
                        st_in().set_binary(
                            vars['x'], vars['y']
                        ),
                        l_not().set(
                            st_nin().set_binary(
                                vars['x'], vars['y']
                            )
                        )
                    )
                )
            )
        )
```

In the next prototype we would like to reduce this to

```
self._formula = (
    forall(
        vars.universal('x'),
        forall(
            vars.universal('y'),
            FOL.equiv(
                ST.in(
                    vars['x'], vars['y']
                ),
                FOL.l_not(
                    ST.nin(
                        vars['x'], vars['y']
                    )
                )
            )
        )
    )
)
```