import unittest
from ..action import (
    action,
    Action_Error,
    get_all_supported_action_additional_argument_types,
    register_supported_action_additional_argument_type,
    unregister_all_supported_action_additional_argument_types,
    is_game_action,
    get_additional_action_argument_types,
    can_invoke_bound_action,
    invoke_bound_action,
)
from ..game_object import Game_Object


class Test(unittest.TestCase):
    def tearDown(self):
        unregister_all_supported_action_additional_argument_types()

    def test_general(self):

        # no type must be registered in advance
        self.assertEqual(
            get_all_supported_action_additional_argument_types(), (Game_Object,)
        )

        # @action() must have at least (self, context)
        with self.assertRaises(TypeError):

            class Test_Class_With_Action:
                @action()
                def on_test_action():
                    pass

        with self.assertRaises(TypeError):

            class Test_Class_With_Action:
                @action()
                def on_test_action(self):
                    pass

        with self.assertRaises(TypeError):

            class Test_Class_With_Action:
                @action()
                def on_test_action(s, context):
                    pass

        with self.assertRaises(TypeError):

            class Test_Class_With_Action:
                @action()
                def on_test_action(self, c):
                    pass

        class Test_Class_With_Action:
            @action()
            def on_test_action(self, context):
                pass

        # additional arguments must be annotated with valid types
        with self.assertRaises(TypeError):

            class Test_Class_With_Action:
                @action()
                def on_test_action(self, context, arg):
                    pass

        with self.assertRaises(TypeError):

            class Test_Class_With_Action:
                @action()
                def on_test_action(self, context, arg):
                    pass

        with self.assertRaises(TypeError):

            class Test_Class_With_Action:
                @action()
                def on_test_action(self, context, arg: "string"):
                    pass

        with self.assertRaises(TypeError):

            class Test_Class_With_Action:
                @action()
                def on_test_action(self, context, arg: int):
                    pass

        register_supported_action_additional_argument_type(int)
        register_supported_action_additional_argument_type(float)

        class Test_Class_With_Action:
            @action()
            def on_test_action1(self, context, arg: int):
                pass

            def on_test_action2(self, context, arg: float):
                pass

        # (can) invoke
        class Test_Class_With_Action:
            @action()
            def on_test_action0(self, context):
                pass

            @action()
            def on_test_action1(self, context, arg1: int):
                pass

            @action()
            def on_test_action2(self, context, arg1: int, arg2: float):
                pass

        test_object = Test_Class_With_Action()
        context = None
        # 0 additional arguments
        self.assertTrue(
            can_invoke_bound_action(
                test_object.on_test_action0, additional_args=[]
            )
        )
        invoke_bound_action(
            test_object.on_test_action0, context=context, additional_args=[]
        )
        # wrong number of additional arguments
        self.assertFalse(
            can_invoke_bound_action(
                test_object.on_test_action0, additional_args=[None]
            )
        )
        with self.assertRaises(Action_Error):
            invoke_bound_action(
                test_object.on_test_action0,
                context=context,
                additional_args=[None],
            )
        # 1 additional argument
        self.assertTrue(
            can_invoke_bound_action(
                test_object.on_test_action1, additional_args=[1]
            )
        )
        invoke_bound_action(
            test_object.on_test_action1, context=context, additional_args=[1]
        )
        # wrong number of additional arguments
        self.assertFalse(
            can_invoke_bound_action(
                test_object.on_test_action1, additional_args=[]
            )
        )
        self.assertFalse(
            can_invoke_bound_action(
                test_object.on_test_action1, additional_args=[1, 2]
            )
        )
        with self.assertRaises(Action_Error):
            invoke_bound_action(
                test_object.on_test_action1, context=context, additional_args=[]
            )
        with self.assertRaises(Action_Error):
            invoke_bound_action(
                test_object.on_test_action1,
                context=context,
                additional_args=[1, 2],
            )
        # wrong type of additional arguments
        self.assertFalse(
            can_invoke_bound_action(
                test_object.on_test_action1, additional_args=[1.0]
            )
        )
        with self.assertRaises(Action_Error):
            invoke_bound_action(
                test_object.on_test_action1,
                context=context,
                additional_args=[1.0],
            )
        # 2 additional arguments
        self.assertTrue(
            can_invoke_bound_action(
                test_object.on_test_action2, additional_args=[1, 2.0]
            )
        )
        invoke_bound_action(
            test_object.on_test_action2,
            context=context,
            additional_args=[1, 2.0],
        )
        # wrong number of additional arguments
        self.assertFalse(
            can_invoke_bound_action(
                test_object.on_test_action2, additional_args=[1]
            )
        )
        self.assertFalse(
            can_invoke_bound_action(
                test_object.on_test_action2, additional_args=[1, 2.0, 3]
            )
        )
        with self.assertRaises(Action_Error):
            invoke_bound_action(
                test_object.on_test_action2,
                context=context,
                additional_args=[1],
            )
        with self.assertRaises(Action_Error):
            invoke_bound_action(
                test_object.on_test_action2,
                context=context,
                additional_args=[1, 2.0, 3],
            )
        # wrong type of additional arguments
        self.assertFalse(
            can_invoke_bound_action(
                test_object.on_test_action2, additional_args=[1.0, 2]
            )
        )
        with self.assertRaises(Action_Error):
            invoke_bound_action(
                test_object.on_test_action2,
                context=context,
                additional_args=[1.0, 2],
            )

        # unregister
        unregister_all_supported_action_additional_argument_types()
        self.assertEqual(
            get_all_supported_action_additional_argument_types(), tuple()
        )
