import {searchConfigs} from "./configSearchModule";
import {clickResultItem} from "./tabSwitcher";

$ = require('jquery')

let displayAnyResult = function () {
    $(searchConfigs.resultListContainer)
    .html('<a class="panel-block is-flex is-flex-direction-row is-justify-content-space-between ' +
        'is-align-items-center"> Any results.</a>')
}

let getMessage = (label, content='') => {
    /*if (content === '') {
        $(searchConfigs.notificatorContent)
        .html(`${content}`)
    }else {
        $(searchConfigs.notificatorContent)
            .html(`<strong>${label}</strong> <br/> <p>${content}</p>`)
    }*/
    console.log(label, content)
}

let search_package = function (packageName, controller) {
    /**
     * Requete de recherche avec promise
     */
    return new Promise(async (resolve, reject) => {
        if ($(searchConfigs.searchInput).val().length !== 0) {
            const { signal } = controller
            let url = '/search/'+packageName

            $(searchConfigs.searchBlockName).addClass('is-loading')

            try {
                const id = setTimeout(() => controller.abort(), searchConfigs.timeOutFetch);

                let response = await fetch(url, {
                    timeout: searchConfigs.timeOutFetch,
                    signal: signal
                })

                if (response.ok || response.status !== 200) {
                    let data = await response.text()
                    resolve(data)
                } else {
                    reject(response)
                }
                clearTimeout(id)
            }catch (e){
                reject(e)
            }
        }
    })
}

export function searchKeyPressListener(){
    /**
     * On veut effectuer la recherche de package avec l'évènement keyup
     */
    $(searchConfigs.searchInput).on('keyup', (event) =>{
        let value = encodeURI($(event.target).val())
        const controller = new AbortController();

        if (value.length !== 0) {
            search_package(value, controller).then((data) => {
                $(searchConfigs.notificator).addClass('is-hidden')

                let inputSearchValue = $(searchConfigs.searchInput).val()

                if (inputSearchValue.length !== 0) { //si la recherche est correcte
                    console.log(data)
                    $(searchConfigs.resultListContainer).html(data)
                    clickResultItem()

                    controller.abort()
                    return new Promise((resolve, reject) => {
                        resolve(data)
                    })
                }else{ //sinon on annule la recherche
                    controller.abort()
                    displayAnyResult()

                    return new Promise((resolve, reject) => {
                        reject()
                    })
                }
            }).catch((error) => {

                if (error instanceof Promise){//Si on arrive pas à se connecter au serveur
                    console.log('A')
                    getMessage(
                        'Impossible de se connecter au serveur',
                        `Error ${error.status}`
                    )
                }else { //Si on a des erreurs
                    console.log('B')
                    let [code, name, message] = [error.code, error.name, error.message]

                    if (typeof error !== 'undefined') { //Si l'erreur est inconnue
                        console.log('B1')
                        if (typeof code == 'number') {
                            if (name === 'AbortError' && code === 20) {
                                message = 'Connection Timeout !!!'
                            }
                            getMessage(`${name} ${code}`, message)
                        }else{
                            getMessage(error)
                        }
                    }else{ //Si l'erreur est connue
                        console.log('B2')
                        getMessage(error)
                    }
                }
                $(searchConfigs.notificator).removeClass('is-hidden')

            }).then((data)=>{
                //console.log('Fin de la requete')
                $(searchConfigs.searchBlockName).removeClass('is-loading')
            }, () => {
                $(searchConfigs.searchBlockName).removeClass('is-loading')
                $(searchConfigs.notificator).removeClass('is-hidden')
            })
        }else {
            $(searchConfigs.searchBlockName).removeClass('is-loading')
            displayAnyResult()
        }

    })
}

