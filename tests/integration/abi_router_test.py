import pyteal as pt


on_completion_actions = pt.BareCallActions(
    opt_in=pt.OnCompleteAction.call_only(pt.Log(pt.Bytes("optin call"))),
    clear_state=pt.OnCompleteAction.call_only(pt.Approve()),
)

router = pt.Router("ASimpleQuestionablyRobustContract", on_completion_actions)
# add_methods_to_router(router)
# (
#     actual_ap_with_oc_compiled,
#     actual_csp_with_oc_compiled,
#     _,
# ) = router.compile_program(version=6)


@router.method
def add(a: pt.abi.Uint64, b: pt.abi.Uint64, *, output: pt.abi.Uint64) -> pt.Expr:
    return output.set(a.get() + b.get())


@router.method
def sub(a: pt.abi.Uint64, b: pt.abi.Uint64, *, output: pt.abi.Uint64) -> pt.Expr:
    return output.set(a.get() - b.get())


@router.method
def mul(a: pt.abi.Uint64, b: pt.abi.Uint64, *, output: pt.abi.Uint64) -> pt.Expr:
    return output.set(a.get() * b.get())


@router.method
def div(a: pt.abi.Uint64, b: pt.abi.Uint64, *, output: pt.abi.Uint64) -> pt.Expr:
    return output.set(a.get() / b.get())


@router.method
def mod(a: pt.abi.Uint64, b: pt.abi.Uint64, *, output: pt.abi.Uint64) -> pt.Expr:
    return output.set(a.get() % b.get())


@router.method
def all_laid_to_args(
    _a: pt.abi.Uint64,
    _b: pt.abi.Uint64,
    _c: pt.abi.Uint64,
    _d: pt.abi.Uint64,
    _e: pt.abi.Uint64,
    _f: pt.abi.Uint64,
    _g: pt.abi.Uint64,
    _h: pt.abi.Uint64,
    _i: pt.abi.Uint64,
    _j: pt.abi.Uint64,
    _k: pt.abi.Uint64,
    _l: pt.abi.Uint64,
    _m: pt.abi.Uint64,
    _n: pt.abi.Uint64,
    _o: pt.abi.Uint64,
    _p: pt.abi.Uint64,
    *,
    output: pt.abi.Uint64,
):
    return output.set(
        _a.get()
        + _b.get()
        + _c.get()
        + _d.get()
        + _e.get()
        + _f.get()
        + _g.get()
        + _h.get()
        + _i.get()
        + _j.get()
        + _k.get()
        + _l.get()
        + _m.get()
        + _n.get()
        + _o.get()
        + _p.get()
    )


@router.method(
    no_op=pt.CallConfig.CALL, opt_in=pt.CallConfig.ALL, clear_state=pt.CallConfig.CALL
)
def empty_return_subroutine() -> pt.Expr:
    return pt.Log(pt.Bytes("appear in both approval and clear state"))


@router.method(
    no_op=pt.CallConfig.CALL, opt_in=pt.CallConfig.CALL, clear_state=pt.CallConfig.CALL
)
def log_1(*, output: pt.abi.Uint64) -> pt.Expr:
    return output.set(1)


@router.method(no_op=pt.CallConfig.CREATE)
def log_creation(*, output: pt.abi.String) -> pt.Expr:
    return output.set("logging creation")


@router.method(no_op=pt.CallConfig.NEVER, clear_state=pt.CallConfig.CALL)
def approve_if_odd(condition_encoding: pt.abi.Uint32) -> pt.Expr:
    return (
        pt.If(condition_encoding.get() % pt.Int(2)).Then(pt.Approve()).Else(pt.Reject())
    )


# rdre = RouterDryRunExecutor(router)


# from pyteal.ast.abi import router

# router.add_method_handler(add)
# router.add_method_handler(sub)
# router.add_method_handler(mul)
# router.add_method_handler(div)
# router.add_method_handler(mod)
# router.add_method_handler(all_laid_to_args)
# router.add_method_handler(
#     empty_return_subroutine,
#     method_config=pt.MethodConfig(
#         no_op=pt.CallConfig.CALL,
#         opt_in=pt.CallConfig.ALL,
#         clear_state=pt.CallConfig.CALL,
#     ),
# )
# router.add_method_handler(
#     log_1,
#     method_config=pt.MethodConfig(
#         no_op=pt.CallConfig.CALL,
#         opt_in=pt.CallConfig.CALL,
#         clear_state=pt.CallConfig.CALL,
#     ),
# )
# router.add_method_handler(
#     log_creation, method_config=pt.MethodConfig(no_op=pt.CallConfig.CREATE)
# )
# router.add_method_handler(
#     approve_if_odd,
#     method_config=pt.MethodConfig(
#         no_op=pt.CallConfig.NEVER, clear_state=pt.CallConfig.CALL
#     ),
# )
