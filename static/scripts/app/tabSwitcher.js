import { searchConfigs } from "./configSearchModule";
import { goToTab } from "./tabManager";

$ = require('jquery')

let goToInfosPackage = (name, version, author, creationDate) => {
    goToTab(0)
}

export function clickResultItem(){
    $(searchConfigs.resultSearchItem).click((e) =>{
        let row = $(e.target).closest('a')
        let inputs = row.find('input')

        let packageName = $(inputs[0]).val()
        let packageVersion = $(inputs[1]).val()
        let packageAuthor = $(inputs[2]).val()
        let packageCreationDate = $(inputs[3]).val()

        //goToInfosPackage(packageName, packageVersion, packageAuthor, packageCreationDate)
    })
}

