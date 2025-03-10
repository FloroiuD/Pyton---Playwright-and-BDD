from pytest_bdd import scenarios
from steps_definition.login import *
from steps_definition.common_steps import *
from steps_definition.contact_search import *


scenarios('features/frontend/')
