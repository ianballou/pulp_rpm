=========
Changelog
=========

..
    You should *NOT* be adding new change log entries to this file, this
    file is managed by towncrier. You *may* edit previous change logs to
    fix problems like typo corrections or such.
    To add a new change log entry, please see
    https://docs.pulpproject.org/en/3.0/nightly/contributing/git.html#changelog-update

    WARNING: Don't drop the next directive!

.. towncrier release notes start

3.0.0b7 (2019-10-16)
====================


Features
--------

- Convert all the TextFields which store JSON content into Django JSONFields.
  `#5215 <https://pulp.plan.io/issues/5215>`_


Improved Documentation
----------------------

- Change the prefix of Pulp services from pulp-* to pulpcore-*
  `#4554 <https://pulp.plan.io/issues/4554>`_
- Docs update to use `pulp_use_system_wide_pkgs`.
  `#5488 <https://pulp.plan.io/issues/5488>`_


Deprecations and Removals
-------------------------

- Change `_id`, `_created`, `_last_updated`, `_href` to `pulp_id`, `pulp_created`, `pulp_last_updated`, `pulp_href`
  `#5457 <https://pulp.plan.io/issues/5457>`_
- Removing `repository` from `Addon`/`Variant` serializers.
  `#5516 <https://pulp.plan.io/issues/5516>`_
- Moved endpoints for distribution trees and repo metadata files to /pulp/api/v3/content/rpm/distribution_trees/ and /pulp/api/v3/content/rpm/repo_metadata_files/ respectively.
  `#5535 <https://pulp.plan.io/issues/5535>`_
- Remove "_" from `_versions_href`, `_latest_version_href`
  `#5548 <https://pulp.plan.io/issues/5548>`_


----


3.0.0b6 (2019-09-30)
====================


Features
--------

- Add upload functionality to the rpm contents endpoints.
  `#5453 <https://pulp.plan.io/issues/5453>`_
- Synchronize and publish modular content.
  `#5493 <https://pulp.plan.io/issues/5493>`_


Bugfixes
--------

- Add url prefix to plugin custom urls.
  `#5330 <https://pulp.plan.io/issues/5330>`_


Deprecations and Removals
-------------------------

- Removing `pulp/api/v3/rpm/upload/`
  `#5453 <https://pulp.plan.io/issues/5453>`_


Misc
----

- `#5172 <https://pulp.plan.io/issues/5172>`_, `#5304 <https://pulp.plan.io/issues/5304>`_, `#5408 <https://pulp.plan.io/issues/5408>`_, `#5421 <https://pulp.plan.io/issues/5421>`_, `#5469 <https://pulp.plan.io/issues/5469>`_, `#5493 <https://pulp.plan.io/issues/5493>`_


----


3.0.0b5 (2019-09-17)
========================


Features
--------

- Setting `code` on `ProgressBar`.
  `#5184 <https://pulp.plan.io/issues/5184>`_
- Sync and Publish kickstart trees.
  `#5206 <https://pulp.plan.io/issues/5206>`_
- Sync and Publish custom/unknown repository metadata.
  `#5432 <https://pulp.plan.io/issues/5432>`_


Bugfixes
--------

- Use the field relative_path instead of filename in the API calls while creating a content from an artifact
  `#4987 <https://pulp.plan.io/issues/4987>`_
- Fixing sync task failure.
  `#5285 <https://pulp.plan.io/issues/5285>`_


Misc
----

- `#4681 <https://pulp.plan.io/issues/4681>`_, `#5201 <https://pulp.plan.io/issues/5201>`_, `#5202 <https://pulp.plan.io/issues/5202>`_, `#5331 <https://pulp.plan.io/issues/5331>`_, `#5430 <https://pulp.plan.io/issues/5430>`_, `#5431 <https://pulp.plan.io/issues/5431>`_, `#5438 <https://pulp.plan.io/issues/5438>`_


----


3.0.0b4 (2019-07-03)
====================


Features
--------

- Add total counts to the sync progress report.
  `#4503 <https://pulp.plan.io/issues/4503>`_
- Greatly speed up publishing of a repository.
  `#4591 <https://pulp.plan.io/issues/4591>`_
- Add ability to copy content between repositories, content type(s) can be specified.
  `#4716 <https://pulp.plan.io/issues/4716>`_
- Renamed Errata/Update content to Advisory to better match the terminology of the RPM/DNF ecosystem.
  `#4902 <https://pulp.plan.io/issues/4902>`_
- Python bindings are now published nightly and with each release as
  `pulp-rpm-client <https://pypi.org/project/pulp-rpm-client/>`_. Also Ruby bindings are published
  similarly to rubygems.org as `pulp_rpm_client <https://rubygems.org/gems/pulp_rpm_client>`_.
  `#4960 <https://pulp.plan.io/issues/4960>`_
- Override the Remote's serializer to allow policy='on_demand' and policy='streamed'.
  `#5065 <https://pulp.plan.io/issues/5065>`_


Bugfixes
--------

- Require relative_path at the content unit creation time.
  `#4835 <https://pulp.plan.io/issues/4835>`_
- Fix migraitons failure by making models compatible with MariaDB.
  `#4909 <https://pulp.plan.io/issues/4909>`_
- Fix unique index length issue for MariaDB.
  `#4916 <https://pulp.plan.io/issues/4916>`_


Improved Documentation
----------------------

- Switch to using `towncrier <https://github.com/hawkowl/towncrier>`_ for better release notes.
  `#4875 <https://pulp.plan.io/issues/4875>`_
- Add a docs page about the Python and Ruby bindings.
  `#4960 <https://pulp.plan.io/issues/4960>`_


Misc
----

- `#4117 <https://pulp.plan.io/issues/4117>`_, `#4567 <https://pulp.plan.io/issues/4567>`_, `#4574 <https://pulp.plan.io/issues/4574>`_, `#5064 <https://pulp.plan.io/issues/5064>`_


----


