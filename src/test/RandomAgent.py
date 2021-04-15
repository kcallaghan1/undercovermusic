class RandomAgent:
    def __init__(self, root, chordType, inversion, extension):
        self.root = root
        self.chordType = chordType
        self.inversion = inversion
        self.extension = extension

    def ChordInfo(self, root, chordType, inversion, extension):
        self.root=root
        self.chordType=chordType
        self.inversion=0
        self.extension=""

    def getRoot(self,root):
        return root

    def setRoot(self, root):
        self.root=root

    def getChordType(self, chordType):
        return chordType

    def setChordType(self, chordType):
        self.chordType=chordType

    def getInversion(self, inversion):
        return inversion

    def setInversion(self, inversion):
        self.inversion=inversion

    def getExtension(self, extension):
        return extension

    def setExtension(self, extension):
        self.extension=extension

    def equals(self, obj):
        if(obj==None):
            return False



#
#
# @Override
# public boolean equals(Object obj){
# if(obj == null){
# return false;
# }
# if(!ChordInfo.class.isAssignableFrom(obj.getClass())){
# return false;
# }
# ChordInfo other = (ChordInfo) obj;
# //TODO: compare inversion and extension (they can be null)
# return this.getRoot().equals(other.getRoot())
# && this.getChordType().equals(other.getChordType());
#
# }
# }
