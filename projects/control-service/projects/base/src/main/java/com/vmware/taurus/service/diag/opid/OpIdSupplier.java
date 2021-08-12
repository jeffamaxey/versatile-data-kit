/*
 * Copyright (c) 2021 VMware, Inc.
 * SPDX-License-Identifier: Apache-2.0
 */

package com.vmware.taurus.service.diag.opid;
@FunctionalInterface
public interface OpIdSupplier  {
    public String getOpId();
}