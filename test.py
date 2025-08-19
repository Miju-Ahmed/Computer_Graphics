def train_one_epoch(args, model, train_loader, optimizer, device, losses):
    model.train()        
    accumulation_steps = 2 
    optimizer.zero_grad()
    # i = 0  <-- REMOVED: This is not needed because enumerate starts at 0 anyway.
    
    # The 'i' from enumerate is all you need.
    for i, (x, y) in enumerate(tqdm(train_loader)):
        batch_size = x.shape[0]
        x, y = x.to(device), y.to(device)

        with torch.no_grad():
            if args.root_rel:
                y = y - y[..., 0:1,]
            else:
                y[..., 2] = y[..., 2] - y[:, 0:1, 0:1, 2]

        pred = model(x)

        # --- Loss Calculation (Unchanged) ---
        loss_3d_pos = loss_mpjpe(pred, y)
        loss_3d_scale = n_mpjpe(pred, y)
        loss_3d_velocity = loss_velocity(pred, y)
        loss_lv = loss_limb_var(pred)
        loss_lg = loss_limb_gt(pred, y)
        loss_a = loss_angle(pred, y)
        loss_av = loss_angle_velocity(pred, y)

        loss_total = loss_3d_pos + \
                    args.lambda_scale * loss_3d_scale + \
                    args.lambda_3d_velocity * loss_3d_velocity + \
                    args.lambda_lv * loss_lv + \
                    args.lambda_lg * loss_lg + \
                    args.lambda_a * loss_a + \
                    args.lambda_av * loss_av 

        # --- Loss Update (Unchanged) ---
        losses['3d_pose'].update(loss_3d_pos.item(), batch_size)
        losses['3d_scale'].update(loss_3d_scale.item(), batch_size)
        losses['3d_velocity'].update(loss_3d_velocity.item(), batch_size)
        losses['lv'].update(loss_lv.item(), batch_size)
        losses['lg'].update(loss_lg.item(), batch_size)
        losses['angle'].update(loss_a.item(), batch_size)
        losses['angle_velocity'].update(loss_av.item(), batch_size)
        losses['total'].update(loss_total.item(), batch_size)

        # --- Gradient Accumulation Logic (Your correct implementation) ---
        loss_total = loss_total / accumulation_steps
        loss_total.backward()
        if(i+1) % accumulation_steps == 0:
            optimizer.step()
            optimizer.zero_grad()
            
        # i += 1 <-- REMOVED: This is not needed because enumerate handles incrementing 'i'.