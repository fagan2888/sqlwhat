from sqlwhat.State import State
from protowhat.Test import TestFail
from protowhat.Reporter import Reporter
from sqlwhat.sct_syntax import SCT_CTX


def test_exercise(
    sct,
    student_code,
    student_result,
    student_conn,
    solution_code,
    solution_result,
    solution_conn,
    pre_exercise_code,
    ex_type,
    error,
    force_diagnose=False,
    debug=False,  # currently unused
):
    """
    """

    state = State(
        student_code=student_code,
        solution_code=solution_code,
        pre_exercise_code=pre_exercise_code,
        student_conn=student_conn,
        solution_conn=solution_conn,
        student_result=student_result,
        solution_result=solution_result,
        reporter=Reporter(errors=error),
        force_diagnose=force_diagnose,
    )

    SCT_CTX["Ex"].root_state = state

    try:
        exec(sct, SCT_CTX)
    except TestFail as tf:
        return tf.payload

    return state.reporter.build_final_payload()
