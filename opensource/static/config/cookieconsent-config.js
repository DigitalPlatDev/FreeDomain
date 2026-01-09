import 'https://cdn.jsdelivr.net/gh/orestbida/cookieconsent@3.1.0/dist/cookieconsent.umd.js';

CookieConsent.run({
    guiOptions: {
        consentModal: {
            layout: "bar inline",
            position: "bottom",
            equalWeightButtons: true,
            flipButtons: false
        },
        preferencesModal: {
            layout: "bar",
            position: "left",
            equalWeightButtons: true,
            flipButtons: false
        }
    },
    categories: {
        necessary: {
            readOnly: true
        },
        functionality: {},
        analytics: {}
    },
    language: {
        default: "en",
        translations: {
            en: {
                consentModal: {
                    title: "We value your privacy",
                    description: "We use cookies to provide essential website functions, enhance your browsing experience, improve our website and analyze our traffic. By clicking Accept All, you consent to our use of cookies.",
                    acceptAllBtn: "Accept all",
                    acceptNecessaryBtn: "Only allow necessary",
                    showPreferencesBtn: "Manage preferences",
                    footer: "<a href=\"https://digitalplat.org/privacy-policy/\">Privacy Policy</a> <a href=\"https://digitalplat.org/cookie-policy/\">Cookie Policy</a>"
                },
                preferencesModal: {
                    title: "Manage Cookie Preferences",
                    acceptAllBtn: "Accept all",
                    acceptNecessaryBtn: "Reject all",
                    savePreferencesBtn: "Save preferences",
                    closeIconLabel: "Close modal",
                    serviceCounterLabel: "Service|Services",
                    sections: [
                        {
                            title: "About Cookies",
                            description: "We use cookies to make our site work properly, provide essential features, personalize your experience, and gather anonymous statistics about website usage."
                        },
                        {
                            title: "Strictly Necessary Cookies <span class=\"pm__badge\">Always Enabled</span>",
                            description: "These cookies are necessary for core functionalities such as domain registration, account login, and security. You cannot disable them.",
                            linkedCategory: "necessary"
                        },
                        {
                            title: "Functionality Cookies",
                            description: "These cookies allow us to remember your preferences and enhance website functionality. Disabling them may impact your experience.",
                            linkedCategory: "functionality"
                        },
                        {
                            title: "Analytics Cookies",
                            description: "Analytics cookies help us understand how visitors interact with our site, so we can improve and offer a better service. Data collected is anonymized and never shared with third parties for advertising.",
                            linkedCategory: "analytics"
                        },
                        {
                            title: "More Information",
                            description: "For any inquiries about our privacy and cookie practices, please refer to our <a href=\"https://digitalplat.org/privacy-policy/\">Privacy Policy</a> or <a href=\"https://digitalplat.org/cookie-policy/\">Cookie Policy</a>."
                        }
                    ]
                }
            }
        }            
    }
});