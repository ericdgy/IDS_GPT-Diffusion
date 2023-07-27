from denoising_diffusion_pytorch import Unet1D, GaussianDiffusion1D, Trainer1D
# from diffusion_utilities import *

model = Unet1D(
    dim=64,
    dim_mults=(1, 2, 4, 8),
    channels=1
)

diffusion = GaussianDiffusion1D(
    model,
    seq_length=10000,
    timesteps=1000,
    objective='pred_v'
)

dataset = TargerDomainDS("address", False)

trainer = Trainer1D(
    diffusion,
    dataset=dataset,
    train_batch_size=32,
    train_lr=8e-5,
    train_num_steps=700000,  # total training steps
    gradient_accumulate_every=2,  # gradient accumulation steps
    ema_decay=0.995,  # exponential moving average decay
    amp=True,  # turn on mixed precision
)

trainer.train()
