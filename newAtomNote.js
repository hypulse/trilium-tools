api.addButtonToToolbar({
  title: "New Atom Note",
  icon: "atom",
  shortcut: "alt+n",
  action: async () => {
    const newAtomNoteId =
      await api.runAsyncOnBackendWithManualTransactionHandling(async () => {
        const atomRootNote = await api.getNoteWithLabel("AtomNotesRoot");
        const today = new Date().toLocaleString("ja-JP", { hour12: false });

        const { note } = await api.createNote(atomRootNote.noteId, today, "");
        note.setLabel("iconClass", "bx bx-atom", false);

        return note.noteId;
      });
    await api.activateNewNote(newAtomNoteId);
  },
});
