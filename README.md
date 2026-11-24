# pytest-mock->used for testing the mock object which simulate the real object behaviour to ensure consistency ,reduce duplication and avoid unexpected behavior.

# In this we have setup and installed pytest-mock by following steps:

**Step1:Creating a virtual environment to avoid version conflict and to use dependencies in isolated manner.
Step2:Activate the virtual environment
Step3:Installing the pytest by using pip statement.
Step4:Installing the pytest-mock by using pip statement.
Step5:Confirming whether the pytest-mock has installed.**


`Mock object is used to simulate real object behavior which is often used in unit testing to test individual component by isolating other component dependencies and becomes predictable by testing the behavior without executing original code.`


`````python`
We use mock objects when:
1.A real object is difficult to create or configure
2.A real object is difficult in time consuming(e.g, accessing to remote database.)
3.A real object has side effect when testing (e.g, sending mails )

In this we use fixtures which are reusable component that can setup and teardown the resources which are needed for tests.Here we use mocker fixtures which can control and create the mock object easy and simplify the tests setup.
````