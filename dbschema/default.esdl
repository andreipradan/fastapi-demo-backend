module default {
	type Item {
		required property name -> str {
            constraint exclusive;
		};
		required property price -> float32;
		property is_offer -> bool;
	}
}
