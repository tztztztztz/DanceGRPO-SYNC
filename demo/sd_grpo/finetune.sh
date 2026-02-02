export WANDB_DISABLED=true
export WANDB_BASE_URL="https://api.wandb.ai"
export WANDB_MODE=online

mkdir images_same

torchrun --nproc_per_node=8 --master_port 19001 \
fastvideo/train_grpo_sd.py --config fastvideo/config_sd/dgx.py:hpsv2
