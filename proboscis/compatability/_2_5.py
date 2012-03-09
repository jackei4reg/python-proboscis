# Copyright (c) 2011 Rackspace
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.


def capture_exception(body_func, *except_type):
    try:
        body_func()
        return None
    except except_type, e:
        return e


def capture_type_error(func):
    try:
        func()
    except TypeError, te:
        if "takes exactly 1 argument" in te.message \
           and "(0 given)" in te.message:
            from proboscis.core import ProboscisTestMethodClassNotDecorated
            raise ProboscisTestMethodClassNotDecorated()
        else:
            raise
