import { UserService } from "@/_generated/api-client"

export async function changeUserPw(oldPw: string, newPw: string) {
    return UserService.changeUserPasswordUserChpwPost(oldPw, newPw)
}
