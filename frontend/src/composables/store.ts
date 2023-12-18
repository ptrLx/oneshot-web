import {reactive} from 'vue'

export const store = reactive({
    profilePicUpdate: 0,
    notifyProfilePicUpdate() {
        this.profilePicUpdate++;
    },
})