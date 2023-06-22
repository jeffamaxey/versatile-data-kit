# Copyright 2021-2023 VMware, Inc.
# SPDX-License-Identifier: Apache-2.0
import logging
from datetime import datetime

from vdk.api.job_input import IJobInput

log = logging.getLogger(__name__)


def run(job_input: IJobInput):
    payload_str = job_input.get_arguments()["payload"]

    log.info(f"Trying to ingest payload: {payload_str}")
    payload = payload_str
    if payload == "None":
        payload = None
    elif payload == "date":
        payload = {"key1": datetime.utcnow()}

    job_input.send_object_for_ingestion(
        payload=payload, destination_table="object_table", method="memory"
    )
