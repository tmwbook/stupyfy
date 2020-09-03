class DisallowsObject:
    def __init__(self, interrupting_playback, seeking, toggling_repeat_context, transferring_playback):
        self.interrupting_playback = interrupting_playback
        self.seeking = seeking
        self.toggling_repeat_context = toggling_repeat_context
        self.transferring_playback = transferring_playback
