# SPDX-license-identifier: Apache-2.0
##############################################################################
# Copyright (c) 2022 Samsung Corporation
# All rights reserved. This program and the accompanying materials
# are made available under the terms of the Apache License, Version 2.0
# which accompanies this distribution, and is available at
# http://www.apache.org/licenses/LICENSE-2.0
##############################################################################

.PHONY: deploy
deploy:
	tox -e docs
	python -m http.server --directory _build/html/
