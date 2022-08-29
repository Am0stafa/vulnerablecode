#
# Copyright (c) nexB Inc. and others. All rights reserved.
# VulnerableCode is a trademark of nexB Inc.
# SPDX-License-Identifier: Apache-2.0
# See http://www.apache.org/licenses/LICENSE-2.0 for the license text.
# See https://github.com/nexB/vulnerablecode for support or download.
# See https://aboutcode.org for more information about nexB OSS projects.
#

from django import forms

from vulnerabilities.models import Package


def get_known_package_types():
    """
    Return a list of known package types.
    """
    pkg_types = [(i.type, i.type) for i in Package.objects.distinct("type").all()]
    pkg_types.append((None, "Any type"))
    return pkg_types


class PackageForm(forms.Form):

    type = forms.ChoiceField(choices=get_known_package_types)
    name = forms.CharField(
        required=False, widget=forms.TextInput(attrs={"placeholder": "Package name or purl"})
    )


class VulnerabilityForm(forms.Form):

    vuln_id = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={"placeholder": "Vulnerability ID or CVE/GHSA"}),
    )
