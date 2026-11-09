# Repository overview

Kestrel moves carrier manifests through intake, normalization, settlement and
reporting. Each module keeps its own source package under `src/kestrel/` and
its own backlog document under `docs/modules/`.

Source markers use the form `# TODO(owner): <text>` or `# FIXME(owner): <text>`.
The backlog documents carry `path:line` entries under their `## Open Work Items`
heading.
