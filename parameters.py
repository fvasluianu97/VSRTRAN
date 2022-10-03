import os


params = {
          "loss": 'chrb',
          "alpha": 1.0,
          "beta": 5.0,
          "gamma": 2.0,
          "delta": 3e-3,
          
          "alpha_perc": 3e-3,
          "alpha_chrb": 1.0,
        
          "lr": 5e-6, #1e-4
          "sched": False, 
          "lambda init": 0.8,
          "lambda step": 20000,

          "bs": 1,
          "margin": 1,
          "crop": True,
          "crop size h": 64,
          "crop size w": 128,
          "crop factor": 1,
          
          "grad_clipping": True,
          "clip value": 1.0, 
          
          "sequence length": 8,
          "eval sequence length": 10,
          "test sequence length": 36,
          "number of workers": 8,
          "eval number of workers": 4,
          "test number of workers": 4,
          
          "generator layers": 2,
          "num_blocks": 4, 
          "block activation": 'prelu',
          "block mode": 'of',
          "sd mode": 'add',
          
          "att type": 'self', 
          "riam": "diff",
          "lerp": True,
          "forget": False,

          "kernel size": 3,
          "filters_s": 64,
          "filters_d": 128,
          "state dimension": 128,
          "shuffle_factor": 4,
          
          "save interval": 100000,
          "eval interval": 5000,
          "test interval": 20000,
          "full test interval": 10000,
          "num_epochs": 10,
          "challenge": False,
          "verbose": True, 
          "model_name": "place_model_name_here",
          "suffix": "",
          "bitrate": "",
          "type": "development",
          "device": "cuda:0",
          "videos_train": 262, 
          "train_startswith": 0,
          "videos_val": 4,
          "val_startswith": 0,
          "videos_test": 4,
          "test_startswith": 0,
          "dataset root": "{}/REDS4_4/".format(os.environ["TMPDIR"]),
          "results dir": "./results",
          "server": "cvl"
          }
