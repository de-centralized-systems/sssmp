# fmt: off

TEST_VECTORS = [
    {
        "s": bytes.fromhex("243f6a8885a308d313198a2e03707344"),
        "n": 1,
        "t": 1,
        "c": [
            bytes.fromhex("243f6a8885a308d313198a2e03707344"),
        ],
        "shares": [
            (1, bytes.fromhex("243f6a8885a308d313198a2e03707344")),
        ],
    },
    {
        "s": bytes.fromhex("243f6a8885a308d313198a2e03707344"),
        "n": 2,
        "t": 1,
        "c": [
            bytes.fromhex("243f6a8885a308d313198a2e03707344"),
        ],
        "shares": [
            (1, bytes.fromhex("243f6a8885a308d313198a2e03707344")),
            (2, bytes.fromhex("243f6a8885a308d313198a2e03707344")),
        ],
    },
    {
        "s": bytes.fromhex("243f6a8885a308d313198a2e03707344"),
        "n": 2,
        "t": 2,
        "c": [
            bytes.fromhex("243f6a8885a308d313198a2e03707344"),
            bytes.fromhex("b7e151628aed2a6ace7500d3cfa9f92a"),
        ],
        "shares": [
            (1, bytes.fromhex("93de3bea0f4e22b9dd6c8afdccd98a6e")),
            (2, bytes.fromhex("51e6c84c8a625c0794f38a9386399a10")),
        ],
    },
    {
        "s": bytes.fromhex("243f6a8885a308d313198a2e03707344"),
        "n": 3,
        "t": 1,
        "c": [
            bytes.fromhex("243f6a8885a308d313198a2e03707344"),
        ],
        "shares": [
            (1, bytes.fromhex("243f6a8885a308d313198a2e03707344")),
            (2, bytes.fromhex("243f6a8885a308d313198a2e03707344")),
            (3, bytes.fromhex("243f6a8885a308d313198a2e03707344")),
        ],
    },
    {
        "s": bytes.fromhex("243f6a8885a308d313198a2e03707344"),
        "n": 3,
        "t": 2,
        "c": [
            bytes.fromhex("243f6a8885a308d313198a2e03707344"),
            bytes.fromhex("b7e151628aed2a6ace7500d3cfa9f92a"),
        ],
        "shares": [
            (1, bytes.fromhex("93de3bea0f4e22b9dd6c8afdccd98a6e")),
            (2, bytes.fromhex("51e6c84c8a625c0794f38a9386399a10")),
            (3, bytes.fromhex("e607992e008f766d5a868a404990633a")),
        ],
    },
    {
        "s": bytes.fromhex("243f6a8885a308d313198a2e03707344"),
        "n": 3,
        "t": 3,
        "c": [
            bytes.fromhex("243f6a8885a308d313198a2e03707344"),
            bytes.fromhex("b7e151628aed2a6abf7158809cf4f3c7"),
            bytes.fromhex("62e7160f38b4da5624cecd28f4ddb05a"),
        ],
        "shares": [
            (1, bytes.fromhex("f1392de537faf8ef88a61f866b5930d9")),
            (2, bytes.fromhex("c25790706a841944e6ee2395ddda78a2")),
            (3, bytes.fromhex("1751d71dd8dde9787d51b63db5f33b3f")),
        ],
    },
    {
        "s": bytes.fromhex("243f6a8885a308d313198a2e03707344"),
        "n": 4,
        "t": 1,
        "c": [
            bytes.fromhex("243f6a8885a308d313198a2e03707344"),
        ],
        "shares": [
            (1, bytes.fromhex("243f6a8885a308d313198a2e03707344")),
            (2, bytes.fromhex("243f6a8885a308d313198a2e03707344")),
            (3, bytes.fromhex("243f6a8885a308d313198a2e03707344")),
            (4, bytes.fromhex("243f6a8885a308d313198a2e03707344")),
        ],
    },
    {
        "s": bytes.fromhex("243f6a8885a308d313198a2e03707344"),
        "n": 4,
        "t": 2,
        "c": [
            bytes.fromhex("243f6a8885a308d313198a2e03707344"),
            bytes.fromhex("b7e151628aed2a6ace7500d3cfa9f92a"),
        ],
        "shares": [
            (1, bytes.fromhex("93de3bea0f4e22b9dd6c8afdccd98a6e")),
            (2, bytes.fromhex("51e6c84c8a625c0794f38a9386399a10")),
            (3, bytes.fromhex("e607992e008f766d5a868a404990633a")),
            (4, bytes.fromhex("ce96351b9b3aa06006d68a4f12e2baec")),
        ],
    },
    {
        "s": bytes.fromhex("243f6a8885a308d313198a2e03707344"),
        "n": 4,
        "t": 3,
        "c": [
            bytes.fromhex("243f6a8885a308d313198a2e03707344"),
            bytes.fromhex("b7e151628aed2a6abf7158809cf4f3c7"),
            bytes.fromhex("62e7160f38b4da5624cecd28f4ddb05a"),
        ],
        "shares": [
            (1, bytes.fromhex("f1392de537faf8ef88a61f866b5930d9")),
            (2, bytes.fromhex("c25790706a841944e6ee2395ddda78a2")),
            (3, bytes.fromhex("1751d71dd8dde9787d51b63db5f33b3f")),
            (4, bytes.fromhex("b4644eeb368faf77af9295ae9cf267a2")),
        ],
    },
    {
        "s": bytes.fromhex("243f6a8885a308d313198a2e03707344"),
        "n": 4,
        "t": 4,
        "c": [
            bytes.fromhex("243f6a8885a308d313198a2e03707344"),
            bytes.fromhex("b7e151628aed2a6abf7158809cf4f3c7"),
            bytes.fromhex("62e7160f38b4da56a784d9045190cfef"),
            bytes.fromhex("324e7738926cfbe5e5f9f878118a1712"),
        ],
        "shares": [
            (1, bytes.fromhex("c3775adda596030aee15f3d2df9e587e")),
            (2, bytes.fromhex("491105ab96c9802db554f2c8f7c927d0")),
            (3, bytes.fromhex("02e61c6ef78fa79c2078ad3f4d367e86")),
            (4, bytes.fromhex("80628a6997d10b12227aaa710eb561eb")),
        ],
    },
    {
        "s": bytes.fromhex("243f6a8885a308d313198a2e03707344"),
        "n": 5,
        "t": 1,
        "c": [
            bytes.fromhex("243f6a8885a308d313198a2e03707344"),
        ],
        "shares": [
            (1, bytes.fromhex("243f6a8885a308d313198a2e03707344")),
            (2, bytes.fromhex("243f6a8885a308d313198a2e03707344")),
            (3, bytes.fromhex("243f6a8885a308d313198a2e03707344")),
            (4, bytes.fromhex("243f6a8885a308d313198a2e03707344")),
            (5, bytes.fromhex("243f6a8885a308d313198a2e03707344")),
        ],
    },
    {
        "s": bytes.fromhex("243f6a8885a308d313198a2e03707344"),
        "n": 5,
        "t": 2,
        "c": [
            bytes.fromhex("243f6a8885a308d313198a2e03707344"),
            bytes.fromhex("b7e151628aed2a6ace7500d3cfa9f92a"),
        ],
        "shares": [
            (1, bytes.fromhex("93de3bea0f4e22b9dd6c8afdccd98a6e")),
            (2, bytes.fromhex("51e6c84c8a625c0794f38a9386399a10")),
            (3, bytes.fromhex("e607992e008f766d5a868a404990633a")),
            (4, bytes.fromhex("ce96351b9b3aa06006d68a4f12e2baec")),
            (5, bytes.fromhex("7977647911d78a0ac8a38a9cdd4b43c6")),
        ],
    },
    {
        "s": bytes.fromhex("243f6a8885a308d313198a2e03707344"),
        "n": 5,
        "t": 3,
        "c": [
            bytes.fromhex("243f6a8885a308d313198a2e03707344"),
            bytes.fromhex("b7e151628aed2a6abf7158809cf4f3c7"),
            bytes.fromhex("62e7160f38b4da5624cecd28f4ddb05a"),
        ],
        "shares": [
            (1, bytes.fromhex("f1392de537faf8ef88a61f866b5930d9")),
            (2, bytes.fromhex("c25790706a841944e6ee2395ddda78a2")),
            (3, bytes.fromhex("1751d71dd8dde9787d51b63db5f33b3f")),
            (4, bytes.fromhex("b4644eeb368faf77af9295ae9cf267a2")),
            (5, bytes.fromhex("6162098684d65f4b342d0006f4db243f")),
        ],
    },
    {
        "s": bytes.fromhex("243f6a8885a308d313198a2e03707344"),
        "n": 5,
        "t": 4,
        "c": [
            bytes.fromhex("243f6a8885a308d313198a2e03707344"),
            bytes.fromhex("b7e151628aed2a6abf7158809cf4f3c7"),
            bytes.fromhex("62e7160f38b4da56a784d9045190cfef"),
            bytes.fromhex("324e7738926cfbe5e5f9f878118a1712"),
        ],
        "shares": [
            (1, bytes.fromhex("c3775adda596030aee15f3d2df9e587e")),
            (2, bytes.fromhex("491105ab96c9802db554f2c8f7c927d0")),
            (3, bytes.fromhex("02e61c6ef78fa79c2078ad3f4d367e86")),
            (4, bytes.fromhex("80628a6997d10b12227aaa710eb561eb")),
            (5, bytes.fromhex("a2854c712ad5e8a0b4b607b79d3d7da2")),
        ],
    },
    {
        "s": bytes.fromhex("243f6a8885a308d313198a2e03707344"),
        "n": 5,
        "t": 5,
        "c": [
            bytes.fromhex("243f6a8885a308d313198a2e03707344"),
            bytes.fromhex("b7e151628aed2a6abf7158809cf4f3c7"),
            bytes.fromhex("62e7160f38b4da56a784d9045190cfef"),
            bytes.fromhex("324e7738926cfbe5f4bf8d8d8c31d763"),
            bytes.fromhex("da06c80abb1185eb645fd38c7831e461"),
        ],
        "shares": [
            (1, bytes.fromhex("197192d71e8786e19b0c55ab3a147c6e")),
            (2, bytes.fromhex("4671310bd3c2081f27d5e839b25bbf3f")),
            (3, bytes.fromhex("d780e0c40995aa45a16f34bf8e997444")),
            (4, bytes.fromhex("7038e787ab61531fb5e2dde3e6471378")),
            (5, bytes.fromhex("88d9e995ad7435461938086cc1dab2af")),
        ],
    },
    {
        "s": bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822"),
        "n": 1,
        "t": 1,
        "c": [
            bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822"),
        ],
        "shares": [
            (1, bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822")),
        ],
    },
    {
        "s": bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822"),
        "n": 2,
        "t": 1,
        "c": [
            bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822"),
        ],
        "shares": [
            (1, bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822")),
            (2, bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822")),
        ],
    },
    {
        "s": bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822"),
        "n": 2,
        "t": 2,
        "c": [
            bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822"),
            bytes.fromhex("b7e151628aed2a6abf7158802933783373a292e3"),
        ],
        "shares": [
            (1, bytes.fromhex("93de3bea0f4e22b9ac68d2ae2a430b77d7abaac1")),
            (2, bytes.fromhex("51e6c84c8a625c0776fb3a3551168322425607ff")),
        ],
    },
    {
        "s": bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822"),
        "n": 3,
        "t": 1,
        "c": [
            bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822"),
        ],
        "shares": [
            (1, bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822")),
            (2, bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822")),
            (3, bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822")),
        ],
    },
    {
        "s": bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822"),
        "n": 3,
        "t": 2,
        "c": [
            bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822"),
            bytes.fromhex("b7e151628aed2a6abf7158802933783373a292e3"),
        ],
        "shares": [
            (1, bytes.fromhex("93de3bea0f4e22b9ac68d2ae2a430b77d7abaac1")),
            (2, bytes.fromhex("51e6c84c8a625c0776fb3a3551168322425607ff")),
            (3, bytes.fromhex("e607992e008f766dc98a62b57825fb1131f4951c")),
        ],
    },
    {
        "s": bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822"),
        "n": 3,
        "t": 3,
        "c": [
            bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822"),
            bytes.fromhex("b7e151628aed2a6abf7158809cf4f3c762e7160f"),
            bytes.fromhex("38b4da56a784d9045190cfefa00c8fe35cf55b72"),
        ],
        "shares": [
            (1, bytes.fromhex("ab6ae1bca8cafbbdfdf81d413f880f609a1b755f")),
            (2, bytes.fromhex("b1008d0f20441517298d2ba496b384700b2563ef")),
            (3, bytes.fromhex("3e55063b0d2de679c76cbccbaa4bf85435372e92")),
        ],
    },
    {
        "s": bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822"),
        "n": 4,
        "t": 1,
        "c": [
            bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822"),
        ],
        "shares": [
            (1, bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822")),
            (2, bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822")),
            (3, bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822")),
            (4, bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822")),
        ],
    },
    {
        "s": bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822"),
        "n": 4,
        "t": 2,
        "c": [
            bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822"),
            bytes.fromhex("b7e151628aed2a6abf7158802933783373a292e3"),
        ],
        "shares": [
            (1, bytes.fromhex("93de3bea0f4e22b9ac68d2ae2a430b77d7abaac1")),
            (2, bytes.fromhex("51e6c84c8a625c0776fb3a3551168322425607ff")),
            (3, bytes.fromhex("e607992e008f766dc98a62b57825fb1131f4951c")),
            (4, bytes.fromhex("ce96351b9b3aa060d9c6f118a7bc888873b74683")),
        ],
    },
    {
        "s": bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822"),
        "n": 4,
        "t": 3,
        "c": [
            bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822"),
            bytes.fromhex("b7e151628aed2a6abf7158809cf4f3c762e7160f"),
            bytes.fromhex("38b4da56a784d9045190cfefa00c8fe35cf55b72"),
        ],
        "shares": [
            (1, bytes.fromhex("ab6ae1bca8cafbbdfdf81d413f880f609a1b755f")),
            (2, bytes.fromhex("b1008d0f20441517298d2ba496b384700b2563ef")),
            (3, bytes.fromhex("3e55063b0d2de679c76cbccbaa4bf85435372e92")),
            (4, bytes.fromhex("63233a0c05a29f20be05b56aab4dbac78071a77f")),
        ],
    },
    {
        "s": bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822"),
        "n": 4,
        "t": 4,
        "c": [
            bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822"),
            bytes.fromhex("b7e151628aed2a6abf7158809cf4f3c762e7160f"),
            bytes.fromhex("38b4da56a784d9045190cfef324e7738926cfbe5"),
            bytes.fromhex("f4bf8d8d8c31d763da06c80aa76e97088bcd17bf"),
        ],
        "shares": [
            (1, bytes.fromhex("5fd56c3124fb2cde27fed54b0aa460b3df4fc277")),
            (2, bytes.fromhex("508f890b2cd7f722a3bd31f4a7fd9d712a456d0a")),
            (3, bytes.fromhex("25ca8cb18829177e7d4ee8ad5156d1b6469be5f0")),
            (4, bytes.fromhex("2a371a2c6556ce93829e65dc06df59ee6fa9fed8")),
        ],
    },
    {
        "s": bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822"),
        "n": 5,
        "t": 1,
        "c": [
            bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822"),
        ],
        "shares": [
            (1, bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822")),
            (2, bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822")),
            (3, bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822")),
            (4, bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822")),
            (5, bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822")),
        ],
    },
    {
        "s": bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822"),
        "n": 5,
        "t": 2,
        "c": [
            bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822"),
            bytes.fromhex("b7e151628aed2a6abf7158802933783373a292e3"),
        ],
        "shares": [
            (1, bytes.fromhex("93de3bea0f4e22b9ac68d2ae2a430b77d7abaac1")),
            (2, bytes.fromhex("51e6c84c8a625c0776fb3a3551168322425607ff")),
            (3, bytes.fromhex("e607992e008f766dc98a62b57825fb1131f4951c")),
            (4, bytes.fromhex("ce96351b9b3aa060d9c6f118a7bc888873b74683")),
            (5, bytes.fromhex("7977647911d78a0a66b7a9988e8ff0bb0015d460")),
        ],
    },
    {
        "s": bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822"),
        "n": 5,
        "t": 3,
        "c": [
            bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822"),
            bytes.fromhex("b7e151628aed2a6abf7158809cf4f3c762e7160f"),
            bytes.fromhex("38b4da56a784d9045190cfefa00c8fe35cf55b72"),
        ],
        "shares": [
            (1, bytes.fromhex("ab6ae1bca8cafbbdfdf81d413f880f609a1b755f")),
            (2, bytes.fromhex("b1008d0f20441517298d2ba496b384700b2563ef")),
            (3, bytes.fromhex("3e55063b0d2de679c76cbccbaa4bf85435372e92")),
            (4, bytes.fromhex("63233a0c05a29f20be05b56aab4dbac78071a77f")),
            (5, bytes.fromhex("ec76b13828cb6c4e50e4220597b5c6e3be63ea02")),
        ],
    },
    {
        "s": bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822"),
        "n": 5,
        "t": 4,
        "c": [
            bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822"),
            bytes.fromhex("b7e151628aed2a6abf7158809cf4f3c762e7160f"),
            bytes.fromhex("38b4da56a784d9045190cfef324e7738926cfbe5"),
            bytes.fromhex("f4bf8d8d8c31d763da06c80aa76e97088bcd17bf"),
        ],
        "shares": [
            (1, bytes.fromhex("5fd56c3124fb2cde27fed54b0aa460b3df4fc277")),
            (2, bytes.fromhex("508f890b2cd7f722a3bd31f4a7fd9d712a456d0a")),
            (3, bytes.fromhex("25ca8cb18829177e7d4ee8ad5156d1b6469be5f0")),
            (4, bytes.fromhex("2a371a2c6556ce93829e65dc06df59ee6fa9fed8")),
            (5, bytes.fromhex("7512169fdaf74463fc0103313b1293b966923342")),
        ],
    },
    {
        "s": bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822"),
        "n": 5,
        "t": 5,
        "c": [
            bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822"),
            bytes.fromhex("b7e151628aed2a6abf7158809cf4f3c762e7160f"),
            bytes.fromhex("38b4da56a784d9045190cfef324e7738926cfbe5"),
            bytes.fromhex("f4bf8d8d8c31d763da06c80abb1185eb4f7c7b57"),
            bytes.fromhex("57f5958490cfd47d7c19bb42ae698bfbad23f815"),
        ],
        "shares": [
            (1, bytes.fromhex("0820f9b5b434f8a35be76e09b8b2f9abb6dd568a")),
            (2, bytes.fromhex("57461a93ef9318b3223674b849e265016ebc3940")),
            (3, bytes.fromhex("75f68aaddba22c9280dc16a34546dca2c57b5601")),
            (4, bytes.fromhex("5a13e96fe17abc404af65970a7396fb65f702b0c")),
            (5, bytes.fromhex("52c37058ce14e2cd487084df83b44feaf6ce43e4")),
        ],
    },
    {
        "s": bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822299f31d0"),
        "n": 1,
        "t": 1,
        "c": [
            bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822299f31d0"),
        ],
        "shares": [
            (1, bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822299f31d0")),
        ],
    },
    {
        "s": bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822299f31d0"),
        "n": 2,
        "t": 1,
        "c": [
            bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822299f31d0"),
        ],
        "shares": [
            (1, bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822299f31d0")),
            (2, bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822299f31d0")),
        ],
    },
    {
        "s": bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822299f31d0"),
        "n": 2,
        "t": 2,
        "c": [
            bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822299f31d0"),
            bytes.fromhex("b7e151628aed2a6abf7158809cf4f3c705de979ae9393686"),
        ],
        "shares": [
            (1, bytes.fromhex("93de3bea0f4e22b9ac68d2ae9f848083a1d7afb8c0a60756")),
            (2, bytes.fromhex("51e6c84c8a625c0776fb3a3520838ed1aeae0d0de0ed5dc7")),
        ],
    },
    {
        "s": bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822299f31d0"),
        "n": 3,
        "t": 1,
        "c": [
            bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822299f31d0"),
        ],
        "shares": [
            (1, bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822299f31d0")),
            (2, bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822299f31d0")),
            (3, bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822299f31d0")),
        ],
    },
    {
        "s": bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822299f31d0"),
        "n": 3,
        "t": 2,
        "c": [
            bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822299f31d0"),
            bytes.fromhex("b7e151628aed2a6abf7158809cf4f3c705de979ae9393686"),
        ],
        "shares": [
            (1, bytes.fromhex("93de3bea0f4e22b9ac68d2ae9f848083a1d7afb8c0a60756")),
            (2, bytes.fromhex("51e6c84c8a625c0776fb3a3520838ed1aeae0d0de0ed5dc7")),
            (3, bytes.fromhex("e607992e008f766dc98a62b5bc777d16ab709a9709d46b41")),
        ],
    },
    {
        "s": bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822299f31d0"),
        "n": 3,
        "t": 3,
        "c": [
            bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822299f31d0"),
            bytes.fromhex("b7e151628aed2a6abf7158809cf4f3c762e7160f38b4da56"),
            bytes.fromhex("a784d9045190cfef324e7738926cfbe57b5692eb99b6a017"),
        ],
        "shares": [
            (1, bytes.fromhex("345ae2ee5edeed569e26a5960de87b66bdb8bcc6889d4b91")),
            (2, bytes.fromhex("fbc0815cd5144d96bed8fdd55e284f68979f6abd0b022820")),
            (3, bytes.fromhex("eba5093a0e69a81333e7d26d50b0474a8e2eee59aa005261")),
        ],
    },
    {
        "s": bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822299f31d0"),
        "n": 4,
        "t": 1,
        "c": [
            bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822299f31d0"),
        ],
        "shares": [
            (1, bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822299f31d0")),
            (2, bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822299f31d0")),
            (3, bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822299f31d0")),
            (4, bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822299f31d0")),
        ],
    },
    {
        "s": bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822299f31d0"),
        "n": 4,
        "t": 2,
        "c": [
            bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822299f31d0"),
            bytes.fromhex("b7e151628aed2a6abf7158809cf4f3c705de979ae9393686"),
        ],
        "shares": [
            (1, bytes.fromhex("93de3bea0f4e22b9ac68d2ae9f848083a1d7afb8c0a60756")),
            (2, bytes.fromhex("51e6c84c8a625c0776fb3a3520838ed1aeae0d0de0ed5dc7")),
            (3, bytes.fromhex("e607992e008f766dc98a62b5bc777d16ab709a9709d46b41")),
            (4, bytes.fromhex("ce96351b9b3aa060d9c6f118458d9275b05c527ca07be9fe")),
        ],
    },
    {
        "s": bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822299f31d0"),
        "n": 4,
        "t": 3,
        "c": [
            bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822299f31d0"),
            bytes.fromhex("b7e151628aed2a6abf7158809cf4f3c762e7160f38b4da56"),
            bytes.fromhex("a784d9045190cfef324e7738926cfbe57b5692eb99b6a017"),
        ],
        "shares": [
            (1, bytes.fromhex("345ae2ee5edeed569e26a5960de87b66bdb8bcc6889d4b91")),
            (2, bytes.fromhex("fbc0815cd5144d96bed8fdd55e284f68979f6abd0b022820")),
            (3, bytes.fromhex("eba5093a0e69a81333e7d26d50b0474a8e2eee59aa005261")),
            (4, bytes.fromhex("500e0a5bfcf9e412d44ac0b5a617bba7c6af832c9aec9af8")),
        ],
    },
    {
        "s": bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822299f31d0"),
        "n": 4,
        "t": 4,
        "c": [
            bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822299f31d0"),
            bytes.fromhex("b7e151628aed2a6abf7158809cf4f3c762e7160f38b4da56"),
            bytes.fromhex("a784d9045190cfef324e7738926cfbe5f4bf8d8d8c31d763"),
            bytes.fromhex("da06c80abb1185eb4f7c7b5757f595848123ea6d925f8f34"),
        ],
        "shares": [
            (1, bytes.fromhex("ee5c2ae4e5cf68bdd15adec15a1deee2b37249cd0f45b3d1")),
            (2, bytes.fromhex("71f09b0c7a9c098ff015085bd0c18b24f915077ba3e6fb50")),
            (3, bytes.fromhex("51875d5cad965aad8b455d5d60a445b7c5a43ce1c4e576e9")),
            (4, bytes.fromhex("6c95daedf3d5f2da927829a9ba1ec1f1e3a5e008706e0b56")),
        ],
    },
    {
        "s": bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822299f31d0"),
        "n": 5,
        "t": 1,
        "c": [
            bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822299f31d0"),
        ],
        "shares": [
            (1, bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822299f31d0")),
            (2, bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822299f31d0")),
            (3, bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822299f31d0")),
            (4, bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822299f31d0")),
            (5, bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822299f31d0")),
        ],
    },
    {
        "s": bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822299f31d0"),
        "n": 5,
        "t": 2,
        "c": [
            bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822299f31d0"),
            bytes.fromhex("b7e151628aed2a6abf7158809cf4f3c705de979ae9393686"),
        ],
        "shares": [
            (1, bytes.fromhex("93de3bea0f4e22b9ac68d2ae9f848083a1d7afb8c0a60756")),
            (2, bytes.fromhex("51e6c84c8a625c0776fb3a3520838ed1aeae0d0de0ed5dc7")),
            (3, bytes.fromhex("e607992e008f766dc98a62b5bc777d16ab709a9709d46b41")),
            (4, bytes.fromhex("ce96351b9b3aa060d9c6f118458d9275b05c527ca07be9fe")),
            (5, bytes.fromhex("7977647911d78a0a66b7a998d97961b2b582c5e64942df78")),
        ],
    },
    {
        "s": bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822299f31d0"),
        "n": 5,
        "t": 3,
        "c": [
            bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822299f31d0"),
            bytes.fromhex("b7e151628aed2a6abf7158809cf4f3c762e7160f38b4da56"),
            bytes.fromhex("a784d9045190cfef324e7738926cfbe57b5692eb99b6a017"),
        ],
        "shares": [
            (1, bytes.fromhex("345ae2ee5edeed569e26a5960de87b66bdb8bcc6889d4b91")),
            (2, bytes.fromhex("fbc0815cd5144d96bed8fdd55e284f68979f6abd0b022820")),
            (3, bytes.fromhex("eba5093a0e69a81333e7d26d50b0474a8e2eee59aa005261")),
            (4, bytes.fromhex("500e0a5bfcf9e412d44ac0b5a617bba7c6af832c9aec9af8")),
            (5, bytes.fromhex("406b823d278401975975ef0da88fb385df1e07c83beee0b9")),
        ],
    },
    {
        "s": bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822299f31d0"),
        "n": 5,
        "t": 4,
        "c": [
            bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822299f31d0"),
            bytes.fromhex("b7e151628aed2a6abf7158809cf4f3c762e7160f38b4da56"),
            bytes.fromhex("a784d9045190cfef324e7738926cfbe5f4bf8d8d8c31d763"),
            bytes.fromhex("da06c80abb1185eb4f7c7b5757f595848123ea6d925f8f34"),
        ],
        "shares": [
            (1, bytes.fromhex("ee5c2ae4e5cf68bdd15adec15a1deee2b37249cd0f45b3d1")),
            (2, bytes.fromhex("71f09b0c7a9c098ff015085bd0c18b24f915077ba3e6fb50")),
            (3, bytes.fromhex("51875d5cad965aad8b455d5d60a445b7c5a43ce1c4e576e9")),
            (4, bytes.fromhex("6c95daedf3d5f2da927829a9ba1ec1f1e3a5e008706e0b56")),
            (5, bytes.fromhex("ec8ea3090cf63807eb517b06a343ade90e5436c2cb54abea")),
        ],
    },
    {
        "s": bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822299f31d0"),
        "n": 5,
        "t": 5,
        "c": [
            bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822299f31d0"),
            bytes.fromhex("b7e151628aed2a6abf7158809cf4f3c762e7160f38b4da56"),
            bytes.fromhex("a784d9045190cfef324e7738926cfbe5f4bf8d8d8c31d763"),
            bytes.fromhex("da06c80abb1185eb4f7c7b5757f5958490cfd47d7c19bb42"),
            bytes.fromhex("158d9554f7b46bced55c4d79fd5f24d64490efe5c811011a"),
        ],
        "shares": [
            (1, bytes.fromhex("fbd1bfb0127b0373040693b8a742ca34e60e9838291286bd")),
            (2, bytes.fromhex("3af8083b9329e3db0fa2b48a9946fdeb5df79e29a6eb5076")),
            (3, bytes.fromhex("0f025b3fb397db37a1aeacf5d47c17ae5264f026b530508c")),
            (4, bytes.fromhex("b01529b0e170d0edfbfd1c1646b6e0b5393298eb8eeebf97")),
            (5, bytes.fromhex("2583c500e9e771fe578803c0a2b4a87bce60aa8fe48c97a5")),
        ],
    },
    {
        "s": bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822299f31d0082efa98"),
        "n": 1,
        "t": 1,
        "c": [
            bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822299f31d0082efa98"),
        ],
        "shares": [
            (1, bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822299f31d0082efa98")),
        ],
    },
    {
        "s": bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822299f31d0082efa98"),
        "n": 2,
        "t": 1,
        "c": [
            bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822299f31d0082efa98"),
        ],
        "shares": [
            (1, bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822299f31d0082efa98")),
            (2, bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822299f31d0082efa98")),
        ],
    },
    {
        "s": bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822299f31d0082efa98"),
        "n": 2,
        "t": 2,
        "c": [
            bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822299f31d0082efa98"),
            bytes.fromhex("b7e151628aed2a6abf7158809cf4f3c762e7160f4973c7a84dac5cf8"),
        ],
        "shares": [
            (1, bytes.fromhex("93de3bea0f4e22b9ac68d2ae9f848083c6ee2e2d60ecf6784582a660")),
            (2, bytes.fromhex("51e6c84c8a625c0776fb3a3520838ed160dc143cbb79a49b926d4273")),
        ],
    },
    {
        "s": bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822299f31d0082efa98"),
        "n": 3,
        "t": 1,
        "c": [
            bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822299f31d0082efa98"),
        ],
        "shares": [
            (1, bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822299f31d0082efa98")),
            (2, bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822299f31d0082efa98")),
            (3, bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822299f31d0082efa98")),
        ],
    },
    {
        "s": bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822299f31d0082efa98"),
        "n": 3,
        "t": 2,
        "c": [
            bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822299f31d0082efa98"),
            bytes.fromhex("b7e151628aed2a6abf7158809cf4f3c762e7160f4973c7a84dac5cf8"),
        ],
        "shares": [
            (1, bytes.fromhex("93de3bea0f4e22b9ac68d2ae9f848083c6ee2e2d60ecf6784582a660")),
            (2, bytes.fromhex("51e6c84c8a625c0776fb3a3520838ed160dc143cbb79a49b926d4273")),
            (3, bytes.fromhex("e607992e008f766dc98a62b5bc777d16023b0233f20a6333dfc11e8b")),
        ],
    },
    {
        "s": bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822299f31d0082efa98"),
        "n": 3,
        "t": 3,
        "c": [
            bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822299f31d0082efa98"),
            bytes.fromhex("b7e151628aed2a6abf7158809cf4f3c762e7160f38b4da56a784d904"),
            bytes.fromhex("5190cfef324e7738926cfbe5f4bf8d8d8c31d76326fcf1789e83c6c0"),
        ],
        "shares": [
            (1, bytes.fromhex("c24ef4053d0055813e04294b6b3b0d0e4adff94e37d71afe3129e55c")),
            (2, bytes.fromhex("0e90d9dd42419be70850fb8cdd498cd3661865abc1317787130766bd")),
            (3, bytes.fromhex("e8e14750fae2c6b5254d58e9b502f29988cea4c7df795ca92a007979")),
        ],
    },
    {
        "s": bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822299f31d0082efa98"),
        "n": 4,
        "t": 1,
        "c": [
            bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822299f31d0082efa98"),
        ],
        "shares": [
            (1, bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822299f31d0082efa98")),
            (2, bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822299f31d0082efa98")),
            (3, bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822299f31d0082efa98")),
            (4, bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822299f31d0082efa98")),
        ],
    },
    {
        "s": bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822299f31d0082efa98"),
        "n": 4,
        "t": 2,
        "c": [
            bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822299f31d0082efa98"),
            bytes.fromhex("b7e151628aed2a6abf7158809cf4f3c762e7160f4973c7a84dac5cf8"),
        ],
        "shares": [
            (1, bytes.fromhex("93de3bea0f4e22b9ac68d2ae9f848083c6ee2e2d60ecf6784582a660")),
            (2, bytes.fromhex("51e6c84c8a625c0776fb3a3520838ed160dc143cbb79a49b926d4273")),
            (3, bytes.fromhex("e607992e008f766dc98a62b5bc777d16023b0233f20a6333dfc11e8b")),
            (4, bytes.fromhex("ce96351b9b3aa060d9c6f118458d927537b8601e1648004627a89155")),
        ],
    },
    {
        "s": bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822299f31d0082efa98"),
        "n": 4,
        "t": 3,
        "c": [
            bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822299f31d0082efa98"),
            bytes.fromhex("b7e151628aed2a6abf7158809cf4f3c762e7160f38b4da56a784d904"),
            bytes.fromhex("5190cfef324e7738926cfbe5f4bf8d8d8c31d76326fcf1789e83c6c0"),
        ],
        "shares": [
            (1, bytes.fromhex("c24ef4053d0055813e04294b6b3b0d0e4adff94e37d71afe3129e55c")),
            (2, bytes.fromhex("0e90d9dd42419be70850fb8cdd498cd3661865abc1317787130766bd")),
            (3, bytes.fromhex("e8e14750fae2c6b5254d58e9b502f29988cea4c7df795ca92a007979")),
            (4, bytes.fromhex("a955716996b691cd3a5cd8ca9c889a7d2f85bf749f20fd5281e0673c")),
        ],
    },
    {
        "s": bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822299f31d0082efa98"),
        "n": 4,
        "t": 4,
        "c": [
            bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822299f31d0082efa98"),
            bytes.fromhex("b7e151628aed2a6abf7158809cf4f3c762e7160f38b4da56a784d904"),
            bytes.fromhex("5190cfef324e7738926cfbe5f4bf8d8d8c31d763da06c80abb1185eb"),
            bytes.fromhex("4f7c7b5757f5958490cfd47d7c19bb42158d9554255efd06f4364a9e"),
        ],
        "shares": [
            (1, bytes.fromhex("8d328f526af5c005aecbfd361722b64c5f526c1aee73de8ae08dece9")),
            (2, bytes.fromhex("405d2c53cca85fabe4720149108123f5ce1ca13d2f323a6466d2178d")),
            (3, bytes.fromhex("5043c860caf6c4481434b8441785516a4b44a6e63601ed2a80c5a695")),
            (4, bytes.fromhex("ef6798758abfeb9b1b5749b8ae92955618a5c5a845737fa8ae2c2636")),
        ],
    },
    {
        "s": bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822299f31d0082efa98"),
        "n": 5,
        "t": 1,
        "c": [
            bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822299f31d0082efa98"),
        ],
        "shares": [
            (1, bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822299f31d0082efa98")),
            (2, bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822299f31d0082efa98")),
            (3, bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822299f31d0082efa98")),
            (4, bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822299f31d0082efa98")),
            (5, bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822299f31d0082efa98")),
        ],
    },
    {
        "s": bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822299f31d0082efa98"),
        "n": 5,
        "t": 2,
        "c": [
            bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822299f31d0082efa98"),
            bytes.fromhex("b7e151628aed2a6abf7158809cf4f3c762e7160f4973c7a84dac5cf8"),
        ],
        "shares": [
            (1, bytes.fromhex("93de3bea0f4e22b9ac68d2ae9f848083c6ee2e2d60ecf6784582a660")),
            (2, bytes.fromhex("51e6c84c8a625c0776fb3a3520838ed160dc143cbb79a49b926d4273")),
            (3, bytes.fromhex("e607992e008f766dc98a62b5bc777d16023b0233f20a6333dfc11e8b")),
            (4, bytes.fromhex("ce96351b9b3aa060d9c6f118458d927537b8601e1648004627a89155")),
            (5, bytes.fromhex("7977647911d78a0a66b7a998d97961b2555f76115f3bc7ee6a04cdad")),
        ],
    },
    {
        "s": bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822299f31d0082efa98"),
        "n": 5,
        "t": 3,
        "c": [
            bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822299f31d0082efa98"),
            bytes.fromhex("b7e151628aed2a6abf7158809cf4f3c762e7160f38b4da56a784d904"),
            bytes.fromhex("5190cfef324e7738926cfbe5f4bf8d8d8c31d76326fcf1789e83c6c0"),
        ],
        "shares": [
            (1, bytes.fromhex("c24ef4053d0055813e04294b6b3b0d0e4adff94e37d71afe3129e55c")),
            (2, bytes.fromhex("0e90d9dd42419be70850fb8cdd498cd3661865abc1317787130766bd")),
            (3, bytes.fromhex("e8e14750fae2c6b5254d58e9b502f29988cea4c7df795ca92a007979")),
            (4, bytes.fromhex("a955716996b691cd3a5cd8ca9c889a7d2f85bf749f20fd5281e0673c")),
            (5, bytes.fromhex("4f24efe42e15cc9f17417baff4c3e437c1537e188168d67cb8e778f8")),
        ],
    },
    {
        "s": bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822299f31d0082efa98"),
        "n": 5,
        "t": 4,
        "c": [
            bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822299f31d0082efa98"),
            bytes.fromhex("b7e151628aed2a6abf7158809cf4f3c762e7160f38b4da56a784d904"),
            bytes.fromhex("5190cfef324e7738926cfbe5f4bf8d8d8c31d763da06c80abb1185eb"),
            bytes.fromhex("4f7c7b5757f5958490cfd47d7c19bb42158d9554255efd06f4364a9e"),
        ],
        "shares": [
            (1, bytes.fromhex("8d328f526af5c005aecbfd361722b64c5f526c1aee73de8ae08dece9")),
            (2, bytes.fromhex("405d2c53cca85fabe4720149108123f5ce1ca13d2f323a6466d2178d")),
            (3, bytes.fromhex("5043c860caf6c4481434b8441785516a4b44a6e63601ed2a80c5a695")),
            (4, bytes.fromhex("ef6798758abfeb9b1b5749b8ae92955618a5c5a845737fa8ae2c2636")),
            (5, bytes.fromhex("fd007bef25d9d2f313d0acded02fcf01fcf460ec706b008a621acf2a")),
        ],
    },
    {
        "s": bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822299f31d0082efa98"),
        "n": 5,
        "t": 5,
        "c": [
            bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822299f31d0082efa98"),
            bytes.fromhex("b7e151628aed2a6abf7158809cf4f3c762e7160f38b4da56a784d904"),
            bytes.fromhex("5190cfef324e7738926cfbe5f4bf8d8d8c31d763da06c80abb1185eb"),
            bytes.fromhex("4f7c7b5757f5958490cfd47d7c19bb42158d9554f7b46bced55c4d79"),
            bytes.fromhex("fd5f24d6613c31c3839a2ddf8a9a276bcfbfa1c898b2817160084b8a"),
        ],
        "shares": [
            (1, bytes.fromhex("706dab840bc9f1c62d51d0e99db8912790edcdd2a42bc933a1efa084")),
            (2, bytes.fromhex("09da5a9c8645622f0c11e71668e2651f8a195f09a6f62e2f2f2ff38c")),
            (3, bytes.fromhex("e49b9a79e127c80f7fcd73c4e57c30ebc0fef91a2fd7b75e4e3d1c9d")),
            (4, bytes.fromhex("13cfb93146ed1603193dab3f6ff8997434f5bcc51304f11fe1319212")),
            (5, bytes.fromhex("fcf77e7d88b71ea8922063869bdfe4481f1bb84986e354bdce2c5b20")),
        ],
    },
    {
        "s": bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822299f31d0082efa98ec4e6c89"),
        "n": 1,
        "t": 1,
        "c": [
            bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822299f31d0082efa98ec4e6c89"),
        ],
        "shares": [
            (1, bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822299f31d0082efa98ec4e6c89")),
        ],
    },
    {
        "s": bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822299f31d0082efa98ec4e6c89"),
        "n": 2,
        "t": 1,
        "c": [
            bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822299f31d0082efa98ec4e6c89"),
        ],
        "shares": [
            (1, bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822299f31d0082efa98ec4e6c89")),
            (2, bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822299f31d0082efa98ec4e6c89")),
        ],
    },
    {
        "s": bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822299f31d0082efa98ec4e6c89"),
        "n": 2,
        "t": 2,
        "c": [
            bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822299f31d0082efa98ec4e6c89"),
            bytes.fromhex("b7e151628aed2a6abf7158809cf4f3c762e7160f38b4da568d973ca0bd1aa0a1"),
        ],
        "shares": [
            (1, bytes.fromhex("93de3bea0f4e22b9ac68d2ae9f848083c6ee2e2d112beb8685b9c6385154cc28")),
            (2, bytes.fromhex("51e6c84c8a625c0776fb3a3520838ed160dc143c59ec9e7c091b82c38d7a37d0")),
        ],
    },
    {
        "s": bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822299f31d0082efa98ec4e6c89"),
        "n": 3,
        "t": 1,
        "c": [
            bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822299f31d0082efa98ec4e6c89"),
        ],
        "shares": [
            (1, bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822299f31d0082efa98ec4e6c89")),
            (2, bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822299f31d0082efa98ec4e6c89")),
            (3, bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822299f31d0082efa98ec4e6c89")),
        ],
    },
    {
        "s": bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822299f31d0082efa98ec4e6c89"),
        "n": 3,
        "t": 2,
        "c": [
            bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822299f31d0082efa98ec4e6c89"),
            bytes.fromhex("b7e151628aed2a6abf7158809cf4f3c762e7160f38b4da568d973ca0bd1aa0a1"),
        ],
        "shares": [
            (1, bytes.fromhex("93de3bea0f4e22b9ac68d2ae9f848083c6ee2e2d112beb8685b9c6385154cc28")),
            (2, bytes.fromhex("51e6c84c8a625c0776fb3a3520838ed160dc143c59ec9e7c091b82c38d7a37d0")),
            (3, bytes.fromhex("e607992e008f766dc98a62b5bc777d16023b02336158442a848cbe6330609771")),
        ],
    },
    {
        "s": bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822299f31d0082efa98ec4e6c89"),
        "n": 3,
        "t": 3,
        "c": [
            bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822299f31d0082efa98ec4e6c89"),
            bytes.fromhex("b7e151628aed2a6abf7158809cf4f3c762e7160f38b4da56a784d9045190cfef"),
            bytes.fromhex("324e7738926cfbe5f4bf8d8d8c31d763da06c80abb1185eb676dea5f8d95cb78"),
        ],
        "shares": [
            (1, bytes.fromhex("a1904cd29d22d95c58d75f2313b557e01ce8e627aa3a6e6dc8c7c9c3304b681e")),
            (2, bytes.fromhex("99c50facf4c99dbe8b3138372647ff4625c4191483a8bcfdda92d6f74c17e8b7")),
            (3, bytes.fromhex("1c6a29f6ec484c31c0ffed3a3682dbe29d25c711000de3401a7be5ac9012ec20")),
        ],
    },
    {
        "s": bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822299f31d0082efa98ec4e6c89"),
        "n": 4,
        "t": 1,
        "c": [
            bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822299f31d0082efa98ec4e6c89"),
        ],
        "shares": [
            (1, bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822299f31d0082efa98ec4e6c89")),
            (2, bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822299f31d0082efa98ec4e6c89")),
            (3, bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822299f31d0082efa98ec4e6c89")),
            (4, bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822299f31d0082efa98ec4e6c89")),
        ],
    },
    {
        "s": bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822299f31d0082efa98ec4e6c89"),
        "n": 4,
        "t": 2,
        "c": [
            bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822299f31d0082efa98ec4e6c89"),
            bytes.fromhex("b7e151628aed2a6abf7158809cf4f3c762e7160f38b4da568d973ca0bd1aa0a1"),
        ],
        "shares": [
            (1, bytes.fromhex("93de3bea0f4e22b9ac68d2ae9f848083c6ee2e2d112beb8685b9c6385154cc28")),
            (2, bytes.fromhex("51e6c84c8a625c0776fb3a3520838ed160dc143c59ec9e7c091b82c38d7a37d0")),
            (3, bytes.fromhex("e607992e008f766dc98a62b5bc777d16023b02336158442a848cbe6330609771")),
            (4, bytes.fromhex("ce96351b9b3aa060d9c6f118458d927537b8601ec97974930a440a2e2e26da3b")),
        ],
    },
    {
        "s": bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822299f31d0082efa98ec4e6c89"),
        "n": 4,
        "t": 3,
        "c": [
            bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822299f31d0082efa98ec4e6c89"),
            bytes.fromhex("b7e151628aed2a6abf7158809cf4f3c762e7160f38b4da56a784d9045190cfef"),
            bytes.fromhex("324e7738926cfbe5f4bf8d8d8c31d763da06c80abb1185eb676dea5f8d95cb78"),
        ],
        "shares": [
            (1, bytes.fromhex("a1904cd29d22d95c58d75f2313b557e01ce8e627aa3a6e6dc8c7c9c3304b681e")),
            (2, bytes.fromhex("99c50facf4c99dbe8b3138372647ff4625c4191483a8bcfdda92d6f74c17e8b7")),
            (3, bytes.fromhex("1c6a29f6ec484c31c0ffed3a3682dbe29d25c711000de3401a7be5ac9012ec20")),
            (4, bytes.fromhex("c31a04b678a089b200c3f9105db04d1f38d854be8c72fca18882910fbbab79d9")),
        ],
    },
    {
        "s": bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822299f31d0082efa98ec4e6c89"),
        "n": 4,
        "t": 4,
        "c": [
            bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822299f31d0082efa98ec4e6c89"),
            bytes.fromhex("b7e151628aed2a6abf7158809cf4f3c762e7160f38b4da56a784d9045190cfef"),
            bytes.fromhex("324e7738926cfbe5f4bf8d8d8c31d763da06c80abb1185eb4f7c7b5757f59584"),
            bytes.fromhex("90cfd47d7c19bb42158d9554f7b46bced55c4d79fd5f24d6cbfb4aff81805e5a"),
        ],
        "shares": [
            (1, bytes.fromhex("315f98afe13b621e4d5aca77e4013c2ec9b4ab5e57654abb2b2d12346bab68b8")),
            (2, bytes.fromhex("75e7f569390132982335fca1df908a6cd71247f12a668717784fc26e6de04d8c")),
            (3, bytes.fromhex("2d13c95b4ecfefc20375ef1b3c74a494727c61806c4524bed7608df6c128967a")),
            (4, bytes.fromhex("e21195c44aba869937e383ccd452c854e93292d7b3583fb02e2d5f30b9bc84f1")),
        ],
    },
    {
        "s": bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822299f31d0082efa98ec4e6c89"),
        "n": 5,
        "t": 1,
        "c": [
            bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822299f31d0082efa98ec4e6c89"),
        ],
        "shares": [
            (1, bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822299f31d0082efa98ec4e6c89")),
            (2, bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822299f31d0082efa98ec4e6c89")),
            (3, bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822299f31d0082efa98ec4e6c89")),
            (4, bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822299f31d0082efa98ec4e6c89")),
            (5, bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822299f31d0082efa98ec4e6c89")),
        ],
    },
    {
        "s": bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822299f31d0082efa98ec4e6c89"),
        "n": 5,
        "t": 2,
        "c": [
            bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822299f31d0082efa98ec4e6c89"),
            bytes.fromhex("b7e151628aed2a6abf7158809cf4f3c762e7160f38b4da568d973ca0bd1aa0a1"),
        ],
        "shares": [
            (1, bytes.fromhex("93de3bea0f4e22b9ac68d2ae9f848083c6ee2e2d112beb8685b9c6385154cc28")),
            (2, bytes.fromhex("51e6c84c8a625c0776fb3a3520838ed160dc143c59ec9e7c091b82c38d7a37d0")),
            (3, bytes.fromhex("e607992e008f766dc98a62b5bc777d16023b02336158442a848cbe6330609771")),
            (4, bytes.fromhex("ce96351b9b3aa060d9c6f118458d927537b8601ec97974930a440a2e2e26da3b")),
            (5, bytes.fromhex("7977647911d78a0a66b7a998d97961b2555f7611f1cdaec587d3368e933c7a9a")),
        ],
    },
    {
        "s": bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822299f31d0082efa98ec4e6c89"),
        "n": 5,
        "t": 3,
        "c": [
            bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822299f31d0082efa98ec4e6c89"),
            bytes.fromhex("b7e151628aed2a6abf7158809cf4f3c762e7160f38b4da56a784d9045190cfef"),
            bytes.fromhex("324e7738926cfbe5f4bf8d8d8c31d763da06c80abb1185eb676dea5f8d95cb78"),
        ],
        "shares": [
            (1, bytes.fromhex("a1904cd29d22d95c58d75f2313b557e01ce8e627aa3a6e6dc8c7c9c3304b681e")),
            (2, bytes.fromhex("99c50facf4c99dbe8b3138372647ff4625c4191483a8bcfdda92d6f74c17e8b7")),
            (3, bytes.fromhex("1c6a29f6ec484c31c0ffed3a3682dbe29d25c711000de3401a7be5ac9012ec20")),
            (4, bytes.fromhex("c31a04b678a089b200c3f9105db04d1f38d854be8c72fca18882910fbbab79d9")),
            (5, bytes.fromhex("46b522ec6021583d4b0d2c1d4d7569bb80398abb0fd7a31c486ba25467ae7d4e")),
        ],
    },
    {
        "s": bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822299f31d0082efa98ec4e6c89"),
        "n": 5,
        "t": 4,
        "c": [
            bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822299f31d0082efa98ec4e6c89"),
            bytes.fromhex("b7e151628aed2a6abf7158809cf4f3c762e7160f38b4da56a784d9045190cfef"),
            bytes.fromhex("324e7738926cfbe5f4bf8d8d8c31d763da06c80abb1185eb4f7c7b5757f59584"),
            bytes.fromhex("90cfd47d7c19bb42158d9554f7b46bced55c4d79fd5f24d6cbfb4aff81805e5a"),
        ],
        "shares": [
            (1, bytes.fromhex("315f98afe13b621e4d5aca77e4013c2ec9b4ab5e57654abb2b2d12346bab68b8")),
            (2, bytes.fromhex("75e7f569390132982335fca1df908a6cd71247f12a668717784fc26e6de04d8c")),
            (3, bytes.fromhex("2d13c95b4ecfefc20375ef1b3c74a494727c61806c4524bed7608df6c128967a")),
            (4, bytes.fromhex("e21195c44aba869937e383ccd452c854e93292d7b3583fb02e2d5f30b9bc84f1")),
            (5, bytes.fromhex("4224f59d44cd730b76aa32e92b70da7f025392855d42a26108c64824c4b77464")),
        ],
    },
    {
        "s": bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822299f31d0082efa98ec4e6c89"),
        "n": 5,
        "t": 5,
        "c": [
            bytes.fromhex("243f6a8885a308d313198a2e03707344a4093822299f31d0082efa98ec4e6c89"),
            bytes.fromhex("b7e151628aed2a6abf7158809cf4f3c762e7160f38b4da56a784d9045190cfef"),
            bytes.fromhex("324e7738926cfbe5f4bf8d8d8c31d763da06c80abb1185eb4f7c7b5757f59584"),
            bytes.fromhex("90cfd47d7c19bb42158d9554f7b46bced55c4d79fd5f24d6613c31c3839a2ddf"),
            bytes.fromhex("8a9a276bcfbfa1c877c56284dab79cd4c2b3293d20e9e5ea5f5e90a925056a6e"),
        ],
        "shares": [
            (1, bytes.fromhex("bbc5bfc42e84c3d63a9fa8f33eb6a0fa0b078263778caf51deb4f9a14cb47153")),
            (2, bytes.fromhex("0d84b3837d04ccac12d18639d015898343d7e10c1c745535d8baf4eb1b600272")),
            (3, bytes.fromhex("dfeaa8dac575b03e4554f707e9463baf240aee407abe137653a8516e9cebf15c")),
            (4, bytes.fromhex("237b99e666eafff40a21628f24daf8266ad61c9efe63b0a6a5a33208031162b2")),
            (5, bytes.fromhex("09d4ded4a722abae3cadb12e014f76d9430435f13090c89da624c89471d62d66")),
        ],
    },
]
