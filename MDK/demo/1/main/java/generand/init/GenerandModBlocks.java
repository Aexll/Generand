
/*
 *    MCreator note: This file will be REGENERATED on each build.
 */
package generand.init;

import net.minecraftforge.registries.RegistryObject;
import net.minecraftforge.registries.ForgeRegistries;
import net.minecraftforge.registries.DeferredRegister;
import generand.GenerandMod;
import generand.block.TestOreBlock;
import net.minecraft.world.level.block.Block;

public class GenerandModBlocks {
	public static final DeferredRegister<Block> REGISTRY = DeferredRegister.create(ForgeRegistries.BLOCKS, GenerandMod.MODID);
	public static final RegistryObject<Block> TEST_ORE = REGISTRY.register("test_ore", () -> new TestOreBlock());
}
