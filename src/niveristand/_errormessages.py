init_var_invalid_type = "TODOMSG: Variables must be initialized with a valid Veristand datatype"
invalid_nested_funcdef = "TODOMSG: Nested function definitions only allowed in multitask"
invalid_top_level_func = "TODOMSG: invalid top level function"
save_without_valid_sequence = "TODOMSG: no valid rtseq to save"
invalid_type_for_operator = "TODOMSG: this operator doesn't support the given type"
name_constant_not_supported = "TODOMSG: this name constant is not supported"
invalid_return_type = "TODOMSG: return statement has invalid type"
invalid_return_value = "TODOMSG: return statement uses undeclared value"
invalid_type_to_convert = "TODOMSG: conversion attempted on an invalid type"
dependency_not_found = "TODOMSG: dependency not found"
invalid_type_for_channel_ref = "TODOMSG: channel references do not support the given type"
unsupported_orelse_while = "TODOMSG: else block not supported in while loops"
return_unsupported_unless_last = "TODOMSG: return statement only supported as last statement in function."
break_unsupported = "TODOMSG: break statements not supported."
variable_reassignment = "TODOMSG: you cannot reassign an already created variable"
cannot_change_array_elements = "TODOMSG: you cannot change individual elements in an array. " \
                               "Change only the value of the element"
param_description_no_param = "TODOMSG: parameter definition for undeclared parameter"
invalid_function_definition = "TODOMSG: unsupported element found in function definition"
invalid_param_decorator = "TODOMSG: parameter description decorator doesn't follow rules"
unexpected_argument_redefine = "TODOMSG: unexpected argument added to list"
invalid_nivs_yield = "TODOMSG: nivs_yield can only be used as a stand-alone statement"
invalid_with_block = "TODOMSG: with can only be used for multitask"
for_else_not_supported = "TODOMSG: else structure in for not supported"
invalid_iterable_collection = "TODOMSG: the iterable collection can only be a variable or a range(end)"
invalid_for_loop_iterator = "TODOMSG: you specified an invalid iterator variable"
invalid_range_call = "TODOMSG: range can only be called with the end value"
scalar_iterable_collection = "TODOMSG: a for loop can only iterate on ArrayType, you specified a scalar variable"
invalid_stmt_after_try = "TODMSG: invalid statement after try. Only return allowed"
try_must_be_first_stmt = "TODOMSG: try must be the first statement in the functiondef"
invalid_try_except_orelse = "TODOMSG: except and orelse clauses not supported. Only try/finally."
return_not_supported_in_try_finally = "TODOMSG: return statement not supported inside a try/finally clause. Put the " \
                                      "return after the finally and it will be executed in the CleanUp section."
try_only_in_top_level_func = "TODOMSG: the use of try is not allowed in this context. Use try/finally only in the top" \
                             "level function."
invalid_taskname_for_stop_task = "TODOMSG: the task name provided is invalid."
unregistered_thread = "TODOMSG: unregistered thread found"
reregister_thread = "TODOMSG: thread tried to register twice"
ref_param_not_ref = "TODOMSG: a parameter marked as pass by reference was not of valid object type."
invalid_error_code_for_generate_error = "TODOMSG: invalid error code provided. Provide an integer number as an error " \
                                        "code. "
invalid_message_for_generate_error = "TODOMSG: invalid message provided. Provide a string message."
invalid_action_for_generate_error = "TODOMSG: invalid error action provided. Provide an error action from ErrorAction" \
                                    "enum."
unknown_identifier = "TODOMSG: undefined identifier '%s' found."
run_without_valid_sequence = "TODOMSG: no valid rtseq to run"
invalid_path_for_sequence = "TODOMSG: the path provided is not a valid rt sequence path"
run_aborted = "TODOMSG: the real-time sequence was stopped or aborted during run"
run_failed = "TODOMSG: the real-time sequence failed"
csharp_call_failed = "TODOMSG: the call into the C# API failed with error code %d. Message: %s"
channel_not_found = "TOMOMSG: a channel with name %s could not be found"
multiple_return_statements = "TODOMSG: there is more than one return statement in this function"
none_not_supported = "TODOMSG: NoneType not supported"
invalid_decorator = "TODOMSG: custom decorators are not allowed"
cascaded_comparison_operators_not_allowed = "TODOMSG: cascading comparison operators is not allowed because of their" \
                                            "different behaviors between Python and SPE"
invalid_operand_for_boolean_operator = "TODOMSG: the type of the operand is invalid for boolean operators"
invalid_type_for_if_test = "TODOMSG: the type of the operand cannot be evaluated in the if test"
invalid_operand_for_unary_invert_operator = "TODOMSG: the type of the operand is invalid for the unary invert operator"
