# Spreadsheet Visual Quality

When to read: before finalizing any Google Sheet created, imported, or edited.

## Scope

- Edit: changed cells/objects plus visible neighbors or dependents.
- New, imported, or reference/template-based Sheet: every populated visible sheet and important output/chart; compare equivalent reference views.

For a new Sheet, size/style the authored area as a whole, never the unused grid.

## Final Check

1. Verify values/formulas and native structure, then inspect the Google-rendered Sheet at normal zoom.
2. Fix clipping, awkward wrapping, overlap, unreadable controls, or damaged layout with the smallest change. For an inserted or substantially changed populated column, use Resize a Column in `./reference-batch-update-recipes.md`.
3. Validate formatting is applied properly and consistently (e.g. when styling a table, prefer rules based conditional formatting over manual per-row formatting).
4. Re-read and re-render. Confirm the fix and no unrelated data, structure, dimension, or layout changes.

Never sheet-wide autofit or restyle an edit, import, reference, or template without authorization. Preserve intentional fixed dimensions and report unavoidable clipping.

## Google Sheets Evidence - Visual Verification

Use CUA to check each sheet visually when it is enabled and authenticated.

If CUA is unavailable and the workspace provides the JavaScript package `@oai/artifact-tool`, export the Google Sheet to `.xlsx` and open it with `SpreadsheetFile.importXlsx()`. For each sheet, check the relevant ranges with `workbook.inspect()` and view the PNG previews from `workbook.render()`. Google Sheets features can change during export, so check discrepancies against the native sheet. Avoid PDF exports for this check because their layout can differ.

If both visual checks are unavailable, review the formatting and style metadata through the Google Sheets API and report the limits of that review.
