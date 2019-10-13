import unittest
from ..action import (
    action,
    get_all_supported_action_additional_argument_types,
    register_supported_action_additional_argument_type,
    unregister_all_supported_action_additional_argument_types,
    is_game_action,
    get_additional_action_argument_types,
)


class Test(unittest.TestCase):
    def tearDown(self):
        unregister_all_supported_action_additional_argument_types()

    def test_general(self):

        # no type must be registered in advance
        self.assertEqual(
            get_all_supported_action_additional_argument_types(), tuple()
        )

        # @action must have at least (self, context)
        with self.assertRaises(TypeError):

            class Test_Class_With_Action:
                @action
                def on_test_action():
                    pass

        with self.assertRaises(TypeError):

            class Test_Class_With_Action:
                @action
                def on_test_action(self):
                    pass

        with self.assertRaises(TypeError):

            class Test_Class_With_Action:
                @action
                def on_test_action(s, context):
                    pass

        with self.assertRaises(TypeError):

            class Test_Class_With_Action:
                @action
                def on_test_action(self, c):
                    pass

        class Test_Class_With_Action:
            @action
            def on_test_action(self, context):
                pass

        # additional arguments must be annotated with valid types
        with self.assertRaises(TypeError):

            class Test_Class_With_Action:
                @action
                def on_test_action(self, context, arg):
                    pass

        with self.assertRaises(TypeError):

            class Test_Class_With_Action:
                @action
                def on_test_action(self, context, arg):
                    pass

        with self.assertRaises(TypeError):

            class Test_Class_With_Action:
                @action
                def on_test_action(self, context, arg: "string"):
                    pass

        with self.assertRaises(TypeError):

            class Test_Class_With_Action:
                @action
                def on_test_action(self, context, arg: int):
                    pass

        register_supported_action_additional_argument_type(int)
        register_supported_action_additional_argument_type(float)

        class Test_Class_With_Action:
            @action
            def on_test_action1(self, context, arg: int):
                pass

            def on_test_action2(self, context, arg: float):
                pass

        # unregister
        unregister_all_supported_action_additional_argument_types()
        self.assertEqual(
            get_all_supported_action_additional_argument_types(), tuple()
        )
